import json
from flask_restful import Resource, reqparse

from algorithms.cluster_analysis import ClusterAnalysis
from es.indices.analytics import Analytics
from es.indices.products import Products


class Product(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('request', type=str)
        parser.add_argument('userId', type=int)
        parameters = parser.parse_args()

        request = json.loads(parameters['request'])

        if parameters['userId']:
            request['sort'] = [self.get_sort_script_for_user(parameters['userId'])]

        items = Products.instance().search(json.dumps(request))

        return {'items': items}

    def get_sort_script_for_user(self, user_id):
        cluster_user_ids = ClusterAnalysis().get_cluster_user_ids(user_id)

        user_analytics = Analytics.instance().search({'query': {'terms': {'userId': cluster_user_ids}}})

        product_sort = dict()
        for event in user_analytics:
            if event['event']['productId'] not in product_sort.keys():
                product_sort[event['event']['productId']] = 0

            product_sort[event['event']['productId']] += 1

        script = {'_script': {'order': 'desc', 'type': 'number', "script": {
            'lang': 'painless',
            "source": "double factor = 1.0E-5;try {factor = params.product_sort[doc['_id'].value];} catch (NullPointerException e) {factor =1.0E-5;} return factor;",
            'params': {"product_sort": product_sort}
        }}}

        return script

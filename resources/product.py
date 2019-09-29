from flask_restful import Resource, reqparse
from elasticsearch import Elasticsearch


class Product(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('request', type=str)
        parser.add_argument('userId', type=int)
        parameters = parser.parse_args()

        if parameters['userId']:
            return {'message': 'TODO: products for user should be calculated'}, 500

        es = Elasticsearch(['elasticsearch'], scheme="http", port=9200)
        res = es.search(index="products", body=parameters['request'])

        items = list()
        for hit in res['hits']['hits']:
            product = hit["_source"]
            product['id'] = hit["_id"]
            items.append(product)

        return {'items': items}

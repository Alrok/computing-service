from flask_restful import Resource, reqparse
from parser.product.spider_runner import SpiderRunner


class Integration(Resource):
    output_data = []

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('domain', type=str, required=True)
        parser.add_argument('start_urls', required=True)
        parser.add_argument('follow_links', type=bool, required=False)
        parameters = parser.parse_args()

        if parameters['follow_links'] == 1:
            parameters['follow_links'] = True
        else:
            parameters['follow_links'] = False

        SpiderRunner('schema_org_product',
                     allowed_domains=[parameters['domain']],
                     start_urls=[parameters['start_urls']],
                     follow_links=parameters['follow_links']).run()

        return {'message': 'Product integrations has been started'}

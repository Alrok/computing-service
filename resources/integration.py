from flask_restful import Resource, reqparse
from parser.product.spider_runner import SpiderRunner


class Integration(Resource):
    output_data = []

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('domain', type=str, required=True)
        parameters = parser.parse_args()

        SpiderRunner().run('schema_org_product',
                           allowed_domains=[parameters['domain']],
                           start_urls=['https://www.citrus.ua/smartfony/redmi-note-7-464gb-black-xiaomi-ua-638711.html'])

        return {'message': 'Product integrations has been started'}


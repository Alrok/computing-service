from flask_restful import Resource, reqparse

from es.indices.products import Products


class Product(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('request', type=str)
        parser.add_argument('userId', type=int)
        parameters = parser.parse_args()

        if parameters['userId']:
            return {'message': 'TODO: products for user should be calculated'}, 500

        items = Products.instance().search(parameters['request'])

        return {'items': items}

from datetime import datetime

from flask_restful import Resource, reqparse
from es.indices.analytics import Analytics as AnalyticsIndex


class Analytics(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True)
        parser.add_argument('event', type=dict, required=True)
        parameters = parser.parse_args()
        parameters['timestamp'] = datetime.now()

        AnalyticsIndex.instance().create(parameters)

        return {"message": "The event has been saved"}

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('request', type=str)
        parameters = parser.parse_args()

        if parameters['userId']:
            return {'message': 'TODO: products for user should be calculated'}, 500

        items = AnalyticsIndex.instance().search(parameters['request'])

        return {'items': items}

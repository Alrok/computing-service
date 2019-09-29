from flask_restful import Resource, reqparse


class Analytics(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True)
        parser.add_argument('event', type=str, required=True)
        parameters = parser.parse_args()

        # TOOD: Save to elasticsearch

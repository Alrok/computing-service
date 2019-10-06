from flask_restful import Resource, reqparse

from es.indices.analytics import Analytics


class UserAnalytics(Resource):

    def get(self, id):
        items = Analytics.instance().search({'query': {'term': {'userId': id}}})

        return {'items': items}

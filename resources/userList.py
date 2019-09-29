from flask_restful import Resource, reqparse
from models.db.user import UserModel


class UserList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), UserModel.query.all()))}

from flask_restful import Resource, reqparse
from models.db.user import UserModel


class User(Resource):
    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json()

        return {'message': 'User not found'}, 404

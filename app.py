from flask import Flask
from flask_restful import Resource, Api

from resources.analytics import Analytics
from resources.product import Product
from resources.user import User
from resources.userAnalytics import UserAnalytics
from resources.userList import UserList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@mysql/shop_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(User, '/user/<int:id>')
api.add_resource(UserList, '/userList')

api.add_resource(Product, '/products/search')

api.add_resource(Analytics, '/analytics')
api.add_resource(UserAnalytics, '/analytics/user/<int:id>')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    app.run(debug=True, host='0.0.0.0')

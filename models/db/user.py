from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

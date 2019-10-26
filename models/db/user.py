from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    gender = db.Column(db.Integer())
    dateOfBirth = db.Column(db.String(255))

    def __init__(self, name, email, gender, dateOfBirth):
        self.name = name
        self.email = email
        self.gender = gender
        self.dateOfBirth = dateOfBirth

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'gender': self.gender, 'dateOfBirth': self.dateOfBirth}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


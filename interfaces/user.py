from app import db
from flask.ext.restful import Resource, marshal, reqparse, abort
from models import User


class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        return marshal(user, User.marshal_fields)


class UserListAPI(Resource):
    def get(self):
        users = User.query.all()
        return [marshal(user, User.marshal_fields) for user in users]


class CurrentUserAPI(Resource):
    def post(self):
        rp = reqparse.RequestParser(bundle_errors=True)
        rp.add_argument('name', type=str, location='json', required=True)
        args = rp.parse_args()

        user = User()
        user.name = args['name']
        db.session.add(user)
        db.session.commit()

        return marshal(user, User.marshal_fields)

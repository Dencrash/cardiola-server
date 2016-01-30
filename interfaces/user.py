from app import db
from flask.ext.restful import Resource, marshal, reqparse
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
        rp.add_argument('chest_pain', type=str, location='json', required=False)
        rp.add_argument('angina', type=bool, location='json', required=False)
        rp.add_argument('eck_result', type=str, location='json', required=False)
        rp.add_argument('blood_sugar', type=bool, location='json', required=False)
        args = rp.parse_args()

        user = User()
        user.name = args['name']
        user.chest_pain = args.get('chest_pain', '')
        user.angina = args.get('angina', False)
        user.eck_result = args.get('eck_result', '')
        user.blood_sugar = args.get('blood_sugar', False)
        db.session.add(user)
        db.session.commit()

        return marshal(user, User.marshal_fields)

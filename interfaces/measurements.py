from app import db
from flask.ext.restful import Resource, marshal, reqparse, abort
from models import Measurement, FrequencyMeasurement, User


class MeasurementAPI(Resource):
    reqparse = reqparse.RequestParser(bundle_errors=True)
    reqparse.add_argument('user_id', type=int, location='json', required=True)
    reqparse.add_argument('time', type=str, location='json', required=True)

    def get(self, type):
        if type == 'rate':
            result = FrequencyMeasurement.query.all()
        elif type == 'pressure':
            result = Measurement.query.all()
        else:
            return abort(400)

        return [marshal(entry, entry.marshal_fields) for entry in result]

    def post(self, type):
        if type == 'rate':
            self.reqparse.add_argument('rate', type=int, location='json', required=True)
        elif type == 'pressure':
            self.reqparse.add_argument('pulse', type=int, location='json', required=True)
            self.reqparse.add_argument('pressure', type=int, location='json', required=True)
        else:
            return abort(400)
        args = self.reqparse.parse_args()

        user = User.query.get(args['user_id'])
        if not user:
            return abort(400)

        if type == 'rate':
            result = FrequencyMeasurement()
            result.user = user
            result.rate = args['rate']
        else:
            result = Measurement()
            result.user = user
            result.pulse = args['pulse']
            result.pressure = args['pressure']

        db.session.add(result)
        db.session.commit()

        return marshal(result, result.marshal_fields)


class UserMeasurementAPI(Resource):

    def get(self, user_id, type):
        if type == 'rate':
            result = FrequencyMeasurement.query.filter(FrequencyMeasurement.user_id == user_id).all()
        elif type == 'pressure':
            result = Measurement.query.filter(Measurement.user_id == user_id).all()
        else:
            return abort(400)

        return [marshal(entry, entry.marshal_fields) for entry in result]

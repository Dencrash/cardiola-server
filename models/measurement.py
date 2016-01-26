from flask.ext.restful import fields
from app import db


class Measurement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='measurements')

    pulse = db.Column(db.Integer)
    pressure = db.Column(db.Integer)

    marshal_fields = {
        'id': fields.Integer(default=0),
        'pulse': fields.Integer,
        'pressure': fields.Integer,
        'timestamp': fields.String
    }


class FrequencyMeasurement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='measurements_frequency')

    rate = db.Column(db.Integer)

    marshal_fields = {
        'id': fields.Integer(default=0),
        'rate': fields.Integer,
        'timestamp': fields.String
    }


class FrequencyMeasurementDaily(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='measurements_frequency_daily')

    rate_min = db.Column(db.Integer)
    rate_max = db.Column(db.Integer)
    rate_avg = db.Column(db.Integer)

    marshal_fields = {
        'id': fields.Integer(default=0),
        'rate_min': fields.Integer,
        'rate_max': fields.Integer,
        'rate_avg': fields.Integer,
        'date': fields.String
    }
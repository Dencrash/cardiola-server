from flask.ext.restful import fields
from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    measurements = db.relationship('Measurement', back_populates='user')
    measurements_frequency = db.relationship('FrequencyMeasurement', back_populates='user')
    measurements_frequency_daily = db.relationship('FrequencyMeasurementDaily', back_populates='user')
    plans = db.relationship('Plan', back_populates='user')

    marshal_fields = {
        'id': fields.Integer(default=0),
        'name': fields.String
    }

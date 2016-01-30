from flask.ext.restful import fields
from app import db


class User(db.Model):

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    measurements = db.relationship('Measurement', back_populates='user')
    measurements_frequency = db.relationship('FrequencyMeasurement', back_populates='user')
    measurements_frequency_daily = db.relationship('FrequencyMeasurementDaily', back_populates='user')
    plans = db.relationship('Plan', back_populates='user')

    chest_pain = db.Column(db.Boolean())
    eck_result = db.Column(db.Integer())
    blood_sugar = db.Column(db.Integer())
    angina = db.Column(db.Boolean())

    marshal_fields = {
        'uid': fields.Integer(default=0),
        'name': fields.String,
        'chest_pain': fields.Boolean,
        'eck_result': fields.Integer,
        'blood_sugar': fields.Integer,
        'angina': fields.Boolean,
    }

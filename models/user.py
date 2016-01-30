from flask.ext.restful import fields
from app import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    measurements = db.relationship('Measurement', back_populates='user',
                                   cascade='all, delete-orphan')
    measurements_frequency = db.relationship('FrequencyMeasurement', back_populates='user',
                                             cascade='all, delete-orphan')
    measurements_frequency_daily = db.relationship('FrequencyMeasurementDaily', back_populates='user',
                                                   cascade='all, delete-orphan')
    plans = db.relationship('Plan', back_populates='user',
                            cascade='all, delete-orphan')

    age = db.Column(db.Integer())
    chest_pain = db.Column(db.String())
    eck_result = db.Column(db.String())
    blood_sugar = db.Column(db.Boolean())
    angina = db.Column(db.Boolean())

    marshal_fields = {
        'uid': fields.Integer(default=0),
        'name': fields.String,
        'chest_pain': fields.String,
        'eck_result': fields.String,
        'blood_sugar': fields.Boolean,
        'angina': fields.Boolean,
    }

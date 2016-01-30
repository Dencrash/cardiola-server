from flask.ext.restful import fields
from app import db


class Measurement(db.Model):

    mid = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    user = db.relationship('User', back_populates='measurements')

    pulse = db.Column(db.Integer)
    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)

    marshal_fields = {
        'mid': fields.Integer(default=0),
        'pulse': fields.Integer,
        'systolic': fields.Integer,
        'diastolic': fields.Integer,
        'timestamp': fields.String
    }

    def __repr__(self):
        return 'Measurement(%d, %d, %d) at %s' % (self.pulse, self.systolic, self.diastolic, self.timestamp)


class FrequencyMeasurement(db.Model):

    mid = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    user = db.relationship('User', back_populates='measurements_frequency')

    rate = db.Column(db.Integer)

    marshal_fields = {
        'mid': fields.Integer(default=0),
        'rate': fields.Integer,
        'timestamp': fields.String
    }

    def __repr__(self):
        return 'Measurement(%d) at %s' % (self.rate, self.timestamp)


class FrequencyMeasurementDaily(db.Model):

    mid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    user = db.relationship('User', back_populates='measurements_frequency_daily')

    rate_min = db.Column(db.Integer)
    rate_max = db.Column(db.Integer)
    rate_avg = db.Column(db.Integer)

    marshal_fields = {
        'mid': fields.Integer(default=0),
        'rate_min': fields.Integer,
        'rate_max': fields.Integer,
        'rate_avg': fields.Integer,
        'date': fields.String
    }

    def __repr__(self):
        return 'Measurement(%d, %d, %d) at %s' % (self.rate_avg, self.rate_max, self.rate_min, self.timestamp)

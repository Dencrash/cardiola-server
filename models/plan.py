from flask.ext.restful import fields
from app import db
from . import User


class PlanEntry(db.Model):

    eid = db.Column(db.Integer, primary_key=True)

    plan_id = db.Column(db.Integer, db.ForeignKey('plan.pid'))
    plan = db.relationship('Plan', back_populates='entries')

    timestamp = db.Column(db.Time)
    mandatory = db.Column(db.Boolean, default=True)

    marshal_fields = {
        'eid': fields.Integer(default=0),
        'timestamp': fields.String,
        'mandatory': fields.Boolean
    }


class Plan(db.Model):

    pid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    user = db.relationship('User', back_populates='plans')

    entries = db.relationship('PlanEntry', back_populates='plan')

    marshal_fields = {
        'pid': fields.Integer(default=0),
        'entries': fields.Nested(PlanEntry.marshal_fields)
    }

from flask.ext.restful import Resource, marshal
from models import Plan


class PlanAPI(Resource):
    def get(self, plan_id):
        plan = Plan.query.get(plan_id)
        return marshal(Plan, plan.marshal_fields)


class PlanListAPI(Resource):
    def get(self, user_id):
        plans = Plan.query.filter(Plan.user_id == user_id).all()
        return [marshal(plan, Plan.marshal_fields) for plan in plans]

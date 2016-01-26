import sys, os

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

if __name__ == '__main__':
    from interfaces.user import UserAPI, UserListAPI, CurrentUserAPI
    from interfaces.plan import PlanAPI, PlanListAPI
    from interfaces.measurements import MeasurementAPI, UserMeasurementAPI

    api = Api(app, catch_all_404s=True)
    api.add_resource(CurrentUserAPI, '/api/user/', endpoint='user')
    api.add_resource(UserAPI, '/api/user/<user_id>', endpoint='user_list')
    api.add_resource(UserListAPI, '/api/users/', endpoint='users')
    api.add_resource(PlanListAPI, '/api/user/<user_id>/plans', endpoint='user_plans')
    api.add_resource(PlanAPI, '/api/plan/<plan_id>', endpoint='plan')
    api.add_resource(MeasurementAPI, '/api/measurements/<type>', endpoint='measurements')
    api.add_resource(UserMeasurementAPI, '/api/user/<user_id>/measurements/<type>', endpoint='user_measurements')

    app.run(debug=True, host='0.0.0.0')

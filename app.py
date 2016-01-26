from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

api = Api(app, catch_all_404s=True)
# api.add_resource(API, '/api/foo/bar', endpoint='name')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

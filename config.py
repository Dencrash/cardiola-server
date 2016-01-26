import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG_MODE = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
BUNDLE_ERRORS = True

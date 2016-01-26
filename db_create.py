#!/usr/bin/env python
from app import db
from models import *

if __name__ == '__main__':
    db.create_all()
    db.session.commit()

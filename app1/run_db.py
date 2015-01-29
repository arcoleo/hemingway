#!/usr/bin/env python

import json
from model import db, User, Category, Skill, Venue, Location, ActivityType

db.create_all()

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance

def bulk_load(table, obj):
    print '\n'
    with open('db.data/%s.data' % table) as f:
        data = json.loads(f.read())

    for item in data:
        print item.values(),
        get_or_create(db.session, obj, **item)
    print '\n'
    print obj.query.all()

bulk_load('category', Category)
bulk_load('activitytype', ActivityType)
bulk_load('skill', Skill)

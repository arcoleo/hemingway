from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

sql_uri = 'mysql://root@localhost/hemingway'
sqlite_uri = 'sqlite:///hemingway.db'

app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

category_activitytype = db.Table('category_activitytype',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('activitytype_id', db.Integer, db.ForeignKey('activitytype.id'))
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=True)


    #activitytypes = db.relationship('ActivityType', backref='AT', lazy='dynamic')
    category_activitytype = db.relationship('ActivityType',
        secondary=category_activitytype,
        backref=db.backref('categories', lazy='dynamic'))

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<Category %r>' % self.category

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(80), unique=True)

    def __init__(self, skill):
        self.skill = skill

    def __repr__(self):
        return '<Skill %r>' % self.skill

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.String(80), unique=True)

    def __init__(self, venue):
        self.venue = venue

    def __repr__(self):
        return '<Venue %r>' % self.venue

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), unique=True)

    def __init__(self, location):
        self.location = location

    def __repr__(self):
        return '<Location %r>' % self.location

class ActivityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activitytype = db.Column(db.String(80), unique=True)
    #activitytype_id = db.Column(db.Integer, db.ForeignKey('activitytype.id'))
    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


    def __init__(self, activitytype):
        self.activitytype = activitytype

    def __repr__(self):
        return '<ActivityType %r>' % self.activitytype



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique =True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    tag = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Date(), default=func.now())
    author = db.Column(db.Integer,db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)

    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Date(), default=func.now())
    author = db.Column(db.Integer,db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
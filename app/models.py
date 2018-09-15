from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from time import time
from app import create_app


class User(UserMixin, db.Model):
    '''
    UserMixin class that includes generic implementations
    that are appropriate for most user model classes
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))
    pitch = db.relationship('Pitch', backref='author', lazy='dynamic')
    bio = db.Column(db.String(1000))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy="dynamic")
    comments = db.relationship('Comments', backref='user', lazy="dynamic")

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
   
    def __repr__(self):
        return '{}'.format(self.username)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Pitch(db.Model):
    '''
    Pitch class represent the pitches Pitched by 
    users.
    ''' 

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    category = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def retrieve_posts(cls, id):
        pitches = Pitch.filter_by(id=id).all()
        return pitches


    def __repr__(self):
        return '{}'.format(self.body)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

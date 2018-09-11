from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    def set_password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    
    def __repr__(self):
        return f'User {self.username}'


# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User', backref='role', lazy="dynamic")

#     def __repr__(self):
#         return f'User {self.name}'


# class Comments(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     details = db.Column(db.String(255))
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# class Pitch(db.Model):
#     __tablename__ = 'pitches'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     category = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     @classmethod
#     def retrieve_posts(cls, id):
#         pitches = Pitch.filter_by(id=id).all()
#         return pitches
#     '''
#     Pitch class represent the pitches Pitched by 
#     users. 
#     '''

#     def __repr__(self):
#         return '{}'.format(self.body)

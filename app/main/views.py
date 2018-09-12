from flask import render_template,request,redirect,url_for, abort
from . import main
from .forms import ReviewForm, UpdateProfile
from ..models import User
from flask_login import login_required
from .. import db, photos
from flask_login import login_required, current_user
import markdown2  

@main.route('/') 
def index():

    '''
    View root function that returns the index page
    '''
    posts = [
        {
            'author': {'username': 'Sniper'},
            'category':'promotion pitch',
            'pitch': 'it is nice to be able to ring a doorbell and there is someone to answer it and welcome you in!'
        },
        {
            'author': {'username': 'Susan'},
            'category':'Pickup line',
            'pitch': 'The Avengers movie was so cool!'
        },
    ]

    return render_template('index.html', posts=posts)
    
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
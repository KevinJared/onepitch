from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import CommentForm, PostForm, UpdateProfile
from ..models import User,  Pitch
from flask_login import login_required
from .. import db, photos
from flask_login import login_required, current_user
import markdown2


@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root function that returns the index page
    '''
    posts = [{
    'author' : 'Edgar kibet',
    'postedOn' : 'Jan 2, 2018 15:46h',
    'content' : 'Am selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can not handle me at my worst, then you sure as hell do not deserve me at my best.',
    'category' : 'Technology'
    },
    {
    'author' : 'Mercy  Cathre',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'content' : 'Two things are infinite: the universe and human stupidity; and am not sure about the universe.',
    'category': 'Interview'
    },
    {
    'author' : 'Sniper Boy',
    'postedOn' : 'Sep 6, 2018 00:15h',
    'content' : 'A room without books is like a body without a soul.',
    'category' : 'Sales'
    },
    {
    'author' : 'Kevin Jared',
    'postedOn' : 'Sep 6, 2018 00:15h',
    'content' : 'You only live once, but if you do it right, once is enough.',
    'category' : 'Pickuplines'
    },
    {
    'author' : 'Sparta',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'content' : 'If you tell the truth, you do not have to remember anything.',
    'category' : 'Interview '
    },
        {
    'author' : 'brian langat',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'content' : 'A friend is someone who knows all about you and still loves you.',
    'category' : 'Interview '
    },
        {
    'author' : 'collins',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'content' : 'Always forgive your enemies; nothing annoys them so much.',
    'category' : 'Interview '
    },
        {
    'author' : 'Sparta',
    'postedOn' : 'Sep 6, 2018 21:03h',
    'content' : 'a measure of the angle of the blades of a screw propeller, equal to the distance forward a blade would move in one revolution if it exerted no thrust on the medium.',
    'category' : 'Interview'
    },
    ]

    form = PostForm()
    if form.validate_on_submit():
       post = form.post.data
       category = form.category.data

       new_pitch = Pitch(body = post,category = category,user = current_user)

       # save pitch
       db.session.add(new_pitch)
       db.session.commit()

       return redirect(url_for('.index'))
    return render_template('index.html',form=form , posts=posts)
    
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

    return render_template('profile/update.html', form= form)

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

@main.route('/post/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):

    users_post = User.query.filter_by(user_id=id).all()
    return render_template('index.html',users_post = users_post)

@main.route('/technology' ,methods = ['GET','POST'])
def technology():
    technology = Pitch.query.filter_by(category = 'Technology').all()
    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = CommentForm(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('technology.html', technology = technology,form=form)

@main.route('/sales' ,methods = ['GET','POST'])
def technolog():
    sales = Pitch.query.filter_by(category = 'sales').all()
    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = CommentForm(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('technolog.html', form=form)

@main.route('/interview' ,methods = ['GET','POST'])
def interview():
    interview = Pitch.query.filter_by(category = 'Interview').all()

    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = CommentForm(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('interview.html', interview = interview,form=form)
    
@main.route('/interview' ,methods = ['GET','POST'])
def business():
    business = Pitch.query.filter_by(category = 'business').all()
    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = CommentForm(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('business.html', business = business,form=form)
    
@main.route('/pickuplines' ,methods = ['GET','POST'])
def pickuplines():

    form = CommentForm()
    if form.validate_on_submit():
        details = form.details.data
        user = current_user

        new_comment = CommentForm(details = details,pitch_id=id,user =user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    pickuplines = Pitch.query.filter_by(category = 'Pickuplines').all()

    if pickuplines is None:
        abort(404)

    return render_template('pickuplines.html', pickuplines = pickuplines,form=form)

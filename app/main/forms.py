from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField 
from wtforms.validators import Required,Email
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    category = SelectField('Category', choices=[('Technology','Technology'),('Pickuplines','Pickuplines'),('BusinessPitch','Business Pitch'),('Sales','Sales'),('Interview','Interview')])
    post = TextAreaField(('Say something'), validators=[Required()])
    submit = SubmitField(('Submit'))

class CommentForm(FlaskForm):
    details = StringField('Write a comment',validators=[Required()])
    submit = SubmitField('Comment')
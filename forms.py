from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError




class PostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    rate = StringField('How much would you rate your experience? ', validators=[DataRequired()])
    comments = TextAreaField('Comments (if any)', validators=[DataRequired()])
    submit = SubmitField('Post')
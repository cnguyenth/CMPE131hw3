from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    author = StringField('author', validators=[DataRequired()])
    message = StringField('message', validators = [DataRequired()])
    submit = SubmitField('Send')

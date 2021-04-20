from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    """
    A class to represent the fields and buttons for the message form.

    ...

    Attributes
    ----------
    author : str
        author of the message
    message : str
        message that the author wrote
    submit : button
        submits the data in the form
    """
    author = StringField('author', validators=[DataRequired()])
    message = StringField('message', validators = [DataRequired()])
    submit = SubmitField('Send')

from flask import render_template, flash, redirect
from app import myapp_obj
from app.forms import MessageForm
from app.models import User, Messages
from app import db

db.create_all()

@myapp_obj.route('/', methods = ['GET', 'POST'])
def homepage():
        form = MessageForm()
        posts = []
##        posts = [{'author': 'ford',
##                  'message': 'Hello world'},
##                 {'author': 'miguel',
##                  'message': 'Bye world'}
##
##                 ]#TEST CODE

        if form.validate_on_submit():
                user = User(author=form.author.data)
                message = Messages(message=form.message.data)
                db.session.add(user)
                db.session.add(message)
                db.session.commit()
                print(f'{form.author.data}: {form.message.data} ')
        return render_template('homepage.html', posts = posts, form=form)

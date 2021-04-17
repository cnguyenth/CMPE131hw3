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
                if bool(User.query.filter_by(author=form.author.data).first()):
                        user = User.query.filter_by(author=form.author.data).first()
                        message = Messages(message=form.message.data, author = user)
                        db.session.add(message)
                        db.session.commit()
                        print(f'{form.author.data}: {form.message.data} ')
                else:
                        user = User(author=form.author.data)
                        message = Messages(message=form.message.data, author = user)
                        db.session.add(user)
                        db.session.add(message)
                        db.session.commit()
                        print(f'{form.author.data}: {form.message.data} ')

            # output all messages
            # create a list of dictionaries with the following structure
            # [{'author':'carlos', 'message':'Yo! Where you at?!'},
            #  {'author':'Jerry', 'message':'Home. You?'}]
        return render_template('homepage.html', posts = posts, form=form)

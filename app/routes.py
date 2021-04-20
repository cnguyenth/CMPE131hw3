from flask import render_template, flash, redirect
from app import myapp_obj
from app.forms import MessageForm
from app.models import User, Messages
from app import db

db.create_all()

@myapp_obj.route('/', methods = ['GET', 'POST'])
def homepage():
        """
        Adds all data entered into form into database and a list of dictionaries.
        
        Parameters
        ----------
                None

        Returns
        -------
                render_template: passes data necessary for the html file     
        """
        form = MessageForm()

        if form.validate_on_submit():
                if bool(User.query.filter_by(author=form.author.data).first()):
                        user = User.query.filter_by(author=form.author.data).first()
                        message = Messages(message=form.message.data, author = user)
                        db.session.add(message)
                        db.session.commit()
                else:
                        user = User(author=form.author.data)
                        message = Messages(message=form.message.data, author = user)
                        db.session.add(user)
                        db.session.add(message)
                        db.session.commit()

        posts = [{'author': 'Carlos',
                  'message': 'Yo! Where you at?!'},
                 
                 {'author': 'Jerry',
                  'message': 'Home. You?'}
                 ]
        
        post = Messages.query.all()
        for p in post:
                posts.append({'author': p.author, 'message': p.message})

        print(posts)
        return render_template('homepage.html', posts = posts, form=form)

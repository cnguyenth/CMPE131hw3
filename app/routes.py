from flask import render_template, flash, redirect
from app import myapp_obj
from app.forms import MessageForm

@myapp_obj.route('/')
def homepage():
        form = MessageForm()
        posts = {'author': 'ford'} #TEST CODE
        return render_template('homepage.html', post = posts, form=form)

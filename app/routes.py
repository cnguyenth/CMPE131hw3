from flask import render_template, flash, redirect

from app import myapp_obj

@myapp_obj.route('/')
def homepage():
	posts = {'author': 'ford'} #TEST CODE
	return render_template('homepage.html', post = posts)

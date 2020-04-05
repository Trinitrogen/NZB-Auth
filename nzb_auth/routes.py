from flask import render_template, flash, redirect, Response, url_for
from nzb_auth import app
from nzb_auth.forms import LoginForm
from nzb_auth.models import User
from flask_login import current_user, login_user, login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('index.html', title='Home')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return render_template('index.html', title='Home')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/nzb_auth', methods=['GET', 'POST'])
def nzb_auth():
    ''' Placeholder to check authentication. Automatically response 401'''
    if current_user.is_authenticated:
        return Response(status=200)
    return Response(status=401)
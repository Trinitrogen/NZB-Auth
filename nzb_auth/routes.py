from flask import render_template, flash, redirect, Response, url_for
from nzb_auth import app
from nzb_auth.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Trinitrogen'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print(f'Username: {form.username.data} Password: {form.password.data}')
        return redirect(url_for(index))
    #return Response("{'a':'b'}", status=401, mimetype='application/json')
    #return render_template()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/nzb_auth', methods=['GET', 'POST'])
def nzb_auth():
    ''' Placeholder to check authentication. Automatically response 401'''
    return Response(status=401)
    #return Response("{'a':'b'}", status=401, mimetype='application/json')
# ty 

from flask import render_template, request, Blueprint, redirect, url_for, flash 
from .models import User 
from . import db 
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user: 
            if check_password_hash(user.pword, password):
                login_user(user)
                return redirect(url_for('views.home'))
            else: 
                flash('Wrong PW.', category='error')
        else: 
            flash('Email does not exist.', category='error')

    return render_template('login.html')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        p1 = request.form['p1']
        p2 = request.form['p2']

        if len(email) < 10: 
            flash('Email must be at least 10.', category='error')
        elif len(fname)  < 2: 
            flash('First name must be at least 2.', category='error')
        elif len(lname) < 2: 
            flash('last name must be at least 2', category='error')
        elif len(p1) < 7: 
            flash('Password must be at least 7.', category='error')
        elif p1 != p2:
            flash('Passwords do not match.', category='error')
        else: 
            user = User(fname=fname, lname=lname, email=email, pword=generate_password_hash(p1))
            db.session.add(user)
            db.session.commit() 

            login_user(user)
            return redirect(url_for('views.home'))
    
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


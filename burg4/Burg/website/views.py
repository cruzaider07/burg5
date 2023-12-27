# ty 

from flask import render_template, request, Blueprint, session, redirect, url_for
from .models import Message, Item 
from flask_login import current_user
from . import db 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('contact', methods=['GET','POST'])
def contact(): 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_message = Message(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()

    return render_template('contact.html')

@views.route('/about')
def about(): 
    return render_template('about.html')

@views.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'POST':
        qty_no = request.form['qty_no']
        qty_no1 = request.form['qty_no1']
        qty_no2 = request.form['qty_no2']

        qty_no = int(qty_no)
        qty_no1 = int(qty_no1)
        qty_no2 = int(qty_no2)

        session['qty_no'] = qty_no
        session['qty_no1'] = qty_no1
        session['qty_no2'] = qty_no2
        
        burger = Item(name='Meaty-Cheezy Burger')
        burger1 = Item(name='Bacon-Layered Burger')
        burger2 = Item(name='Crispy-Layered Burger')

        for i in range(qty_no):

            db.session.add(Item(name='Meaty-Cheezy Burger'))
            db.session.commit()

        for i in range(qty_no1):

            db.session.add(Item(name='Bacon-Layered Burger'))
            db.session.commit()

        for i in range(qty_no2):

            db.session.add(Item(name='Crispy-Layered Burger'))
            db.session.commit()

        session['burger2'] = burger2
        session['burger1'] = burger1
        session['burger'] = burger

        if not current_user.is_authenticated: 
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('views.ordered'))
        
    return render_template('menu.html', user=current_user)

@views.route('/menu/ordered')
def ordered():
    return render_template(qty_no=session['qty_no'], qty_no1=session['qty_no1'], qty_no2=session['qty_no2'], burger=session['burger'], burger1=session['burger1'], burger2=session['burger2'])
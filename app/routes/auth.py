from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models import Customer, Admin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# Customer Login
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        customer = Customer.query.filter_by(email=email).first()
        if customer and check_password_hash(customer.password, password):
            login_user(customer)
            return redirect(url_for('customer.home'))
        flash('Invalid Credentials', 'danger')
    return render_template('customer/login.html')

# Customer Register
@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        customer = Customer(name=name, email=email, password=password)
        db.session.add(customer)
        db.session.commit()
        flash('Account created. Please login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('customer/register.html')

# Logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

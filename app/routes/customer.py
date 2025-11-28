from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Product, Order
from app import db

customer_bp = Blueprint('customer', __name__)

# Homepage
@customer_bp.route('/')
def home():
    products = Product.query.limit(8).all()
    return render_template('customer/home.html', products=products)

# Product List
@customer_bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('customer/products.html', products=products)

# Product Detail
@customer_bp.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('customer/product_detail.html', product=product)

# Cart
@customer_bp.route('/cart')
@login_required
def cart():
    # Placeholder: Fetch cart from session or DB
    return render_template('customer/cart.html')

# Custom Order Form
@customer_bp.route('/custom-order', methods=['GET','POST'])
@login_required
def custom_order():
    if request.method == 'POST':
        # Process measurements, instructions, upload images
        flash('Custom order submitted successfully!', 'success')
        return redirect(url_for('customer.dashboard'))
    return render_template('customer/custom_order.html')

# Customer Dashboard
@customer_bp.route('/dashboard')
@login_required
def dashboard():
    orders = Order.query.filter_by(customer_id=current_user.id).all()
    return render_template('customer/dashboard.html', orders=orders)

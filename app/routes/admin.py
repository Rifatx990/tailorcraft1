from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import Product, Order, Worker
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin Dashboard
@admin_bp.route('/')
@login_required
def dashboard():
    total_orders = Order.query.count()
    total_products = Product.query.count()
    total_workers = Worker.query.count()
    return render_template('admin/dashboard.html', orders=total_orders, products=total_products, workers=total_workers)

# Product Management
@admin_bp.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

# Add/Edit Product
@admin_bp.route('/product/add', methods=['GET','POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        product = Product(name=name, category=category, price=price)
        db.session.add(product)
        db.session.commit()
        flash('Product added', 'success')
        return redirect(url_for('admin.products'))
    return render_template('admin/add_product.html')

# Orders
@admin_bp.route('/orders')
@login_required
def orders():
    orders = Order.query.all()
    return render_template('admin/orders.html', orders=orders)

# Worker Management
@admin_bp.route('/workers')
@login_required
def workers():
    workers = Worker.query.all()
    return render_template('admin/workers.html', workers=workers)

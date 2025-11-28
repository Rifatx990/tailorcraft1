from flask import Blueprint, jsonify
from app.models import Product

api_bp = Blueprint('api', __name__)

@api_bp.route('/products')
def get_products():
    products = Product.query.all()
    result = []
    for p in products:
        result.append({'id': p.id, 'name': p.name, 'price': p.price})
    return jsonify(result)

from flask import Blueprint, request, jsonify
from models import Product, ProductSchema, db

products_bp = Blueprint('products', __name__, url_prefix='/products')
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    data = request.json
    product.name = data['name']
    product.price = data['price']
    db.session.commit()
    return product_schema.jsonify(product)

@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})

products = [
    {
        'id': 1,
        'name': 'Wireless Mouse',
        'price': 25.99,
        'stock': 15,
        'description': 'Ergonomic wireless mouse with adjustable DPI.'
    },
    {
        'id': 2,
        'name': 'Mechanical Keyboard',
        'price': 89.99,
        'stock': 8,
        'description': 'RGB backlit mechanical keyboard with brown switches.'
    },
    {
        'id': 3,
        'name': 'USB-C Hub',
        'price': 39.99,
        'stock': 20,
        'description': '7-in-1 USB-C Hub with HDMI and card reader.'
    }
]
@products_bp.route('/')
def list_products():
    return jsonify(products)

@products_bp.route('/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

from flask import Blueprint, request, jsonify
from models import Product, ProductSchema, db

products_bp = Blueprint('products', __name__)
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

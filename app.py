from flask import Flask
from extensions import db, ma
from routes.products import products_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)


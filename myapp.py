from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///klimat.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    products = Product.query.filter_by(isActive=True).order_by(
        Product.price.desc()).all()
    return render_template('index.html', data=products)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text)

    def __repr__(self):
        return self.title


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == "__main__":
    # app.app_context().push()
    # db.create_all()
    app.run(debug=True)

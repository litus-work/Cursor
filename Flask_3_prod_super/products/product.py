import os
import uuid

from flask import Blueprint, render_template, request
from wtforms import Form, StringField, validators, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired

from utils import get_data, add_data

product = Blueprint('products', __name__, template_folder='template', static_folder='static',
                    static_url_path='/products/static')
PRODUCT_LIST = "products/prod.json"
LIST = "products/new.json"

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'




class ProductForm(Form):
    name = StringField('Product name', [validators.Length(min=4, max=25)])
    desc = StringField('Description', [validators.Length(min=6, max=350)])
    submit = SubmitField()
    price = IntegerField('price', validators=[DataRequired()])
    id = StringField('Product id', [validators.UUID(message=None)])
    image = FileField()


@product.route('/all_products', methods=['GET'])
def get_all_products():
    return render_template('products.html', data=get_data(PRODUCT_LIST))


@product.route('/products/<product_id>')
def get_item_page(product_id):
    for i in get_data(PRODUCT_LIST):
        print(PRODUCT_LIST)
        if i['id'] == product_id:
            return render_template("product_id.html", name=i['name'],
                                   desc=i['description'],
                                   image=i['img_name'],
                                   price=i['price'],
                                   id=i['id'], path=product.static_url_path)
        else:
            render_template("404_page.html")


@product.route('/products/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    return render_template('add_product.html', form=form)


@product.route('/products/submit', methods=['POST'])
def product_submit():
    form = ProductForm(request.form)
    product_id = str(uuid.uuid4())
    name = form.name.data
    desc = form.desc.data
    price = form.price.data
    img_name = upload_file()
    d = {"id": product_id, "name": name, "description": desc, "price": price, "img_name": img_name}
    print(d)
    data = get_data(PRODUCT_LIST)
    print(data)
    data.append(d)
    print(data)
    add_data(data, PRODUCT_LIST)
    return render_template('submit.html', name=name, desc=desc)


@product.route('/upload', methods=['POST'])
def upload_file():
    if request.files['image']:
        f = request.files['image']
        f.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload', f.filename))
        return f.filename
    else:
        return 'no_image.png'
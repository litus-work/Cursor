from flask import Flask, render_template, request
from supermarkets.supermarket import supermarket
from products.product import product


app = Flask(__name__)
app.register_blueprint(supermarket)
app.register_blueprint(product)



@app.route('/')
def get_home_page():
    return render_template('/home.html')


# @app.route('/test-form')
# def test_form():
#     return render_template('/test-form.html')
#







if __name__ == '__main__':
    app.run(debug=True)

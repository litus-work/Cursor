from flask import Flask, Blueprint, render_template

from utils import get_data

supermarket = Blueprint('supermarkets', __name__, template_folder='template', static_folder='static', static_url_path='/supermarkets/static')
SUPERMARKET_LIST = "supermarkets/super.json"



@supermarket.route('/all_supermarkets', methods=['GET'])
def get_all_supermarkets():
    print(get_data(SUPERMARKET_LIST))
    return render_template('supermarkets.html', data=get_data(SUPERMARKET_LIST))


@supermarket.route('/supermarkets/<supermarket_id>')
def get_item_page(supermarket_id):
    for i in get_data(SUPERMARKET_LIST):
        print(SUPERMARKET_LIST)
        if i['id'] == supermarket_id:
            return render_template("supermarket_id.html", name=i['name'],
                                   image=i['img_name'],
                                   location=i['location'],
                                   id=i['id'], path=supermarket.static_url_path)
        else:
            render_template("404_page.html")





@supermarket.route('/add_supermarket')
def add_supermarketS():
    return 'Ok'

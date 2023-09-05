from flask import Blueprint
from flask import render_template
from models.orders_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route('/orders')
def index():
    return render_template('index.jinja', title="My Orders", orders=orders)

@orders_blueprint.route('/orders/<int:index>')
def view_order(index):
    order = orders[index]
    return render_template('order.jinja', order=order)

@orders_blueprint.route('/names')
def view_names():
    return render_template('link_order.jinja', title="Customer's Names", orders=orders)
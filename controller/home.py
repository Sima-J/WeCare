from flask import render_template
from flask import Blueprint

home_controller = Blueprint('home', __name__)

@home_controller.route('/')
def home_route():
    return render_template('home.html')

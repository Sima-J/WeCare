from flask import render_template
from flask import Blueprint

index_controller = Blueprint('index', __name__)

@index_controller.route('/')
def patient_route():
    return render_template('/index.html')

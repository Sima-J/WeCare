from flask import render_template
from flask import Blueprint

doctor_list_controller = Blueprint('list', __name__)

@doctor_list_controller.route('/doctor/list')
def doctor_route():
    return render_template('/doctor/list.html')

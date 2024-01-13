from flask import render_template
from flask import Blueprint

patient_id_controller = Blueprint('patient_id', __name__)

@patient_id_controller.route('/patient/id')
def patient_route():
    return render_template('/patient/login_id.html')

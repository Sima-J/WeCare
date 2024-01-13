from flask import render_template
from flask import Blueprint

patient_confirmation_controller = Blueprint('patient_confirmation', __name__)

@patient_confirmation_controller.route('/patient/confirmation')
def patient_route():
    return render_template('/patient/confirmation.html')

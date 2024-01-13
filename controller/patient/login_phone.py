from flask import render_template
from flask import Blueprint

patient_phone_controller = Blueprint('patient_phone', __name__)

@patient_phone_controller.route('/patient/phone')
def patient_route():
    return render_template('/patient/login_phone.html')

from flask import render_template
from flask import Blueprint

patient_login_controller = Blueprint('patient_login', __name__)

@patient_login_controller.route('/patient/login')
def patient_route():
    return render_template('/patient/login.html')

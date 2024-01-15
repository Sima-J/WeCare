from flask import render_template
from flask import Blueprint

doctor_profile_controller = Blueprint('patient_profile', __name__)

@doctor_profile_controller.route('/doctor/patient_profile')
def doctor_route():
    return render_template('/doctor/patient_profile.html')

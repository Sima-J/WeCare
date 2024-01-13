from flask import render_template
from flask import Blueprint

patient_symptoms_controller = Blueprint('patient_symptoms', __name__)

@patient_symptoms_controller.route('/patient/symptoms')
def patient_route():
    return render_template('/patient/symptoms.html')

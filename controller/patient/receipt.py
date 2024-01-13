from flask import render_template
from flask import Blueprint

patient_receipt_controller = Blueprint('patient_receipt', __name__)

@patient_receipt_controller.route('/patient/receipt')
def patient_route():
    return render_template('/patient/receipt.html')

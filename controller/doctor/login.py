from flask import render_template
from flask import Blueprint

doctor_login_controller = Blueprint('doctor_login', __name__)

@doctor_login_controller.route('/doctor/login')
def doctor_route():
    return render_template('/doctor/login.html')

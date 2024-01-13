from flask import render_template
from flask import Blueprint

admin_doctor_register_controller = Blueprint('admin_doctor_register', __name__)

@admin_doctor_register_controller.route('/admin/doctor_register')
def admin_route():
    return render_template('/admin/doctor_register.html')
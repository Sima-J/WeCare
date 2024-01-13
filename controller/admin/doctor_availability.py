from flask import render_template
from flask import Blueprint

admin_doctor_availability_controller = Blueprint('admin_doctor_availability', __name__)

@admin_doctor_availability_controller.route('/admin/doctor_availability')
def admin_route():
    return render_template('/admin/doctor_availability.html')
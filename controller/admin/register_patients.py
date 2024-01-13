from flask import render_template
from flask import Blueprint

admin_register_patients_controller = Blueprint('admin_register_patient', __name__)

@admin_register_patients_controller.route('/admin/register_patints')
def admin_route():
    return render_template('/admin/register_patients.html')
from flask import render_template
from flask import Blueprint

admin_patients_records_controller = Blueprint('admin_patients_records', __name__)

@admin_patients_records_controller.route('/admin/patients_records')
def admin_route():
    return render_template('/admin/patients_records.html')
from flask import render_template
from flask import Blueprint

admin_dashboard_controller = Blueprint('admin_dashboard', __name__)

@admin_dashboard_controller.route('/admin/dashboard')
def admin_route():
    return render_template('/admin/dashboard.html')
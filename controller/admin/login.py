from flask import render_template
from flask import Blueprint

admin_login_controller = Blueprint('admin_login', __name__)

@admin_login_controller.route('/admin/login')
def admin_route():
    return render_template('/admin/login.html')
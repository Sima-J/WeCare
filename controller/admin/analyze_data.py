from flask import render_template, Blueprint

admin_analyze_data_controller = Blueprint('admin_analyze_data', __name__)


@admin_analyze_data_controller.route('/admin/analyze_data')
def admin_route():
  

    return render_template('/admin/analyze_data.html')

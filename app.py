from flask import Flask
from controller.patient.login import patient_login_controller
from controller.patient.login_phone import patient_phone_controller
from controller.patient.login_id import patient_id_controller
from controller.patient.symptoms import patient_symptoms_controller
from controller.patient.receipt import patient_receipt_controller
from controller.patient.confirmation import patient_confirmation_controller

from controller.doctor.patient_profile import doctor_profile_controller
from controller.doctor.login import doctor_login_controller
from controller.doctor.list import doctor_list_controller


from controller.admin.analyze_data import admin_analyze_data_controller
from controller.admin.dashboard import admin_dashboard_controller
from controller.admin.doctor_availability import admin_doctor_availability_controller
from controller.admin.doctor_register import admin_doctor_register_controller
from controller.admin.login import admin_login_controller
from controller.admin.patients_records import admin_patients_records_controller
from controller.admin.register_patients import admin_register_patients_controller
from controller.admin.common_illness import admin_common_illness_controller








app = Flask(__name__, static_url_path='/static')
# Patenit controllers
app.register_blueprint(patient_login_controller)
app.register_blueprint(patient_phone_controller)
app.register_blueprint(patient_id_controller)
app.register_blueprint(patient_symptoms_controller)
app.register_blueprint(patient_receipt_controller)
app.register_blueprint(patient_confirmation_controller)


# Admin Controllers

app.register_blueprint(admin_analyze_data_controller)
app.register_blueprint(admin_dashboard_controller)
app.register_blueprint(admin_doctor_availability_controller)
app.register_blueprint(admin_doctor_register_controller)
app.register_blueprint(admin_login_controller)
app.register_blueprint(admin_patients_records_controller)
app.register_blueprint(admin_register_patients_controller)
app.register_blueprint(admin_common_illness_controller)




#Doctor Controllers 
app.register_blueprint(doctor_profile_controller)
app.register_blueprint(doctor_login_controller)
app.register_blueprint(doctor_list_controller)


if __name__ == '__main__':
    app.run(debug=True)

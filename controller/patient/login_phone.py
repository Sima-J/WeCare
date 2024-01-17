from flask import render_template, request, Blueprint
import csv
import os

patient_phone_controller = Blueprint('patient_phone', __name__)

def read_patient_credentials():
    patients_file_path = os.path.join('static', 'users', 'patients_profile.csv')
    patient_credentials = []

    try:
        with open(patients_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                patient_credentials.append({'patient_phone': row[0]})
    except FileNotFoundError:
        print(f"File not found: {patients_file_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return patient_credentials

@patient_phone_controller.route('/patient/phone')
def patient_id_route():
    return render_template('/patient/login_phone.html')

@patient_phone_controller.route('/submit_phone_form', methods=['POST'])
def submit_id_form():
    patient_id = request.form.get('patient_phone')

    patient_credentials = read_patient_credentials()

    authenticate = False

    for patient in patient_credentials:
        if patient['patient_phone'] == patient_id :
            authenticate = True
            # Redirect the user to another page or render a response
            return render_template('patient/symptoms.html', patient_id=patient_id)

    # Authentication failed
    return render_template('patient/login_phone.html', patient_id=patient_id, auth=authenticate)

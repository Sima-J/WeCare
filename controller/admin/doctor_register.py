from flask import render_template,request
from flask import Blueprint
import csv
import os

admin_doctor_register_controller = Blueprint('admin_doctor_register', __name__)

# Function to read username and password from CSV file in the 'static' folder
def read_user_credentials():
    users_file_path = os.path.join('static','users', 'doctors.csv')
    user_credentials = []
    
    with open(users_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # Assuming the CSV file has columns 'username' and 'password'
        for row in csvreader:
            user_credentials.append({'username': row[0], 'password': row[1]})
    
    return user_credentials

@admin_doctor_register_controller.route('/admin/doctor_register')
def admin_route():
    return render_template('/admin/doctor_register.html')

@admin_doctor_register_controller.route('/submit_register_form', methods=['POST'])
def submit_form():

    authenticate = True
    
    doctor_name = request.form.get('doctor_name')
    doctor_birthdate = request.form.get('doctor_birthdate')
    doctor_country = request.form.get('doctor_country')
    doctor_phone = request.form.get('doctor_phone')
    doctor_email = request.form.get('doctor_email')
    doctor_location = request.form.get('doctor_location')
    doctor_marital = request.form.get('doctor_marital')
    doctor_specialized = request.form.get('doctor_specialized')

    # Specify the file path with the 'users' folder inside the 'static' folder
    file_path = os.path.join('static', 'users', 'doctors.csv')
    
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['doctors_name', 'doctor_birthdate', 'doctor_country', 'doctor_phone', 'doctor_email', 'doctor_location', 'doctor_marital', 'doctor_specialized']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Create a dictionary from the variables
        doctor_data = {
            'doctors_name': doctor_name,
            'doctor_birthdate': doctor_birthdate,
            'doctor_country': doctor_country,
            'doctor_phone': doctor_phone,
            'doctor_email': doctor_email,
            'doctor_location': doctor_location,
            'doctor_marital': doctor_marital,
            'doctor_specialized': doctor_specialized
        }

        # Write the header if the file was just created
        if not file_exists:
            writer.writeheader()

        # Insert the data into the CSV file
        writer.writerow(doctor_data)

    authenticate = True

    return render_template('admin/doctor_register.html',auth = authenticate)
from flask import render_template, request, Blueprint
import csv
import os

admin_login_controller = Blueprint('admin_login', __name__)

# Function to read username and password from CSV file in the 'static' folder
def read_user_credentials():
    users_file_path = os.path.join('static','users', 'users.csv')
    user_credentials = []
    
    with open(users_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # Assuming the CSV file has columns 'username' and 'password'
        for row in csvreader:
            user_credentials.append({'username': row[0], 'password': row[1]})
    
    return user_credentials

@admin_login_controller.route('/admin/login')
def admin_route():
    authenticate = True
    return render_template('/admin/login.html', authenticate=True)

@admin_login_controller.route('/submit_form', methods=['POST'])
def submit_form():
    admin_username = request.form.get('admin_username')
    admin_password = request.form.get('admin_password')

    user_credentials = read_user_credentials()

    print(user_credentials)

    authenticate = True

    if any(user['username'] == admin_username and user['password'] == admin_password for user in user_credentials):
        print("Hello")
        authenticate = True
        # You can redirect the user to another page or render a response
        return render_template('admin/dashboard.html', username=admin_username)
    else:
        authenticate = False
        # You can redirect the user to another page or render a response
        return render_template('admin/login.html', username=admin_username,auth = authenticate)

    

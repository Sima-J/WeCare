from flask import Blueprint, render_template
import pandas as pd

admin_analyze_gender_controller = Blueprint('analyze_gender', __name__)

# Load the dataset
dataset = pd.read_csv('static/dataset/patients.csv')

@admin_analyze_gender_controller.route('/admin/analyze_data_gender')
def admin_analyze_gender():
    # Create a mapping between symptoms and related illnesses based on gender
    gender_symptoms_mapping = dataset.groupby(['Gender', 'Symptom1', 'Symptom2', 'Symptom3'])['Illness'].value_counts().reset_index(name='count')

    # Get the most common illness for each gender
    most_common_illness_by_gender = gender_symptoms_mapping.groupby(['Gender', 'Illness'])['count'].sum().reset_index()
    most_common_illness_by_gender = most_common_illness_by_gender.loc[most_common_illness_by_gender.groupby('Gender')['count'].idxmax()]

    # Display the dataset in an HTML table
    table_columns = ['RecordID', 'PatientID', 'PatientName', 'Gender', 'Age', 'Symptom1', 'Level1', 'Symptom2', 'Level2', 'Symptom3', 'Level3', 'Symptom4', 'Level4', 'Doctor', 'Date', 'Time', 'SpecializedDoctor', 'Illness']
    table_html = dataset[table_columns].to_html(classes='table table-striped', index=False)

    return render_template('admin/analyze_data_gender.html', most_common_illness_by_gender=most_common_illness_by_gender, table_html=table_html)

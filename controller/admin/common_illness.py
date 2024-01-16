from flask import Blueprint, render_template
import pandas as pd

admin_common_illness_controller = Blueprint('common_illness', __name__)

# Load the dataset
dataset = pd.read_csv('static/dataset/patients.csv')

@admin_common_illness_controller.route('/admin/common_illness')
def admin_route():
    # Create a mapping between symptoms and related illnesses
    symptoms_mapping = dataset.groupby(['Symptom1', 'Symptom2', 'Symptom3'])['Illness'].value_counts().reset_index(name='count')

    # Get the most common illness
    most_common_illness = symptoms_mapping.groupby('Illness')['count'].sum().idxmax()

    # Display the dataset in an HTML table
    table_html = dataset.to_html(classes='table table-striped', index=False)

    return render_template('admin/common_illness.html', table_html=table_html, most_common_illness=most_common_illness, symptoms_mapping=symptoms_mapping)

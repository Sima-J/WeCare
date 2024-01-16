from flask import Blueprint, render_template, request, flash
import pandas as pd

admin_common_illness_controller = Blueprint('common_illness', __name__)

# Load the dataset
dataset = pd.read_csv('static/dataset/patients.csv')

# Function to handle filtering by date
def filter_dataset_by_date(selected_date_str):
    try:
        # Convert selected date to match dataset format (MM/DD/YYYY)
        selected_date = pd.to_datetime(selected_date_str, format='%Y-%m-%d')

        # Filter dataset by selected date
        filtered_dataset = dataset[dataset['Date'] == selected_date]
        return filtered_dataset
    except ValueError:
        # Handle invalid date format gracefully
        flash('Invalid date format. Please use MM/DD/YYYY format.', 'error')
        return pd.DataFrame(columns=dataset.columns)

@admin_common_illness_controller.route('/admin/common_illness', methods=['GET', 'POST'])
def admin_route():
    # Initialize selected_date
    selected_date = None

    # Handle filtering by date
    if request.method == 'POST':
        selected_date_str = request.form.get('selected_date')

        # Ensure a date is selected
        if selected_date_str:
            filtered_dataset = filter_dataset_by_date(selected_date_str)
            if not filtered_dataset.empty:
                selected_date = pd.to_datetime(selected_date_str).strftime('%Y-%m-%d')
        else:
            filtered_dataset = dataset
    else:
        filtered_dataset = dataset

    # Create a mapping between symptoms and related illnesses
    symptoms_mapping = filtered_dataset.groupby(['Symptom1', 'Symptom2', 'Symptom3'])['Illness'].value_counts().reset_index(name='count')

    # Check if symptoms_mapping is empty
    if symptoms_mapping.empty:
        most_common_illness_info = "No data available"
    else:
        # Get the most common illness
        most_common_illness = symptoms_mapping.groupby('Illness')['count'].sum().idxmax()

        # Get the symptoms associated with the most common illness
        common_illness_symptoms = symptoms_mapping[symptoms_mapping['Illness'] == most_common_illness]

        # Get the doctors visited for the most common illness
        visited_doctors = filtered_dataset[filtered_dataset['Illness'] == most_common_illness]['Doctor'].unique()

        # Create a dictionary with information about the most common illness
        most_common_illness_info = {
            'illness': most_common_illness,
            'symptoms': common_illness_symptoms[['Symptom1', 'Symptom2', 'Symptom3']].values.tolist(),
            'visited_doctors': visited_doctors.tolist()
        }

    # Display the dataset in an HTML table
    table_html = filtered_dataset.to_html(classes='min-w-full bg-white border border-gray-300 divide-y divide-gray-200', index=False)

    return render_template('admin/common_illness.html', table_html=table_html,
                           most_common_illness_info=most_common_illness_info,
                           selected_date=selected_date, filtered_dataset=filtered_dataset)

# ... (any other routes, initialization, etc.)

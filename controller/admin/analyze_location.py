from flask import render_template, Blueprint
import pandas as pd

admin_analyze_location_controller = Blueprint('admin_analyze_location', __name__)

# Load the dataset
# Assuming the dataset is loaded into a pandas DataFrame named 'df'
# Replace 'path/to/your/dataset.csv' with the actual path to your CSV file
dataset = pd.read_csv('static/dataset/location.csv')

@admin_analyze_location_controller.route('/admin/analyze_location')
def admin_route():
    # Analyze data based on location and other related factors
    location_analysis = analyze_location_data(dataset)

    return render_template('/admin/location.html', location_analysis=location_analysis)

def analyze_location_data(df):
    # Perform analysis on the dataset based on location and other factors
    # You can customize this analysis based on your specific requirements

    # Example: Calculate average number of cases per location
    avg_cases_per_location = df.groupby('Location')['Number_of_Cases'].mean()

    # Example: Calculate the total population per location
    total_population_per_location = df.groupby('Location')['Population'].sum()

    # Example: Calculate the average economic index per location
    avg_economic_index_per_location = df.groupby('Location')['Economic_Index'].mean()

    # Example: Find the most common illness by location
    most_common_illness_by_location = df.groupby(['Location', 'Zone'])['Patient_Illness'].apply(lambda x: x.mode().iloc[0])

    # Create a dictionary to store the analysis results
    location_analysis = {
        'avg_cases_per_location': avg_cases_per_location,
        'total_population_per_location': total_population_per_location,
        'avg_economic_index_per_location': avg_economic_index_per_location,
        'most_common_illness_by_location': most_common_illness_by_location,
    }

    return location_analysis

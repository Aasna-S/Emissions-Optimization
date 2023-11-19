import streamlit as st
import pandas as pd

# Path to the Excel file
file_path = "https://raw.githubusercontent.com/[Aasna-S]/[repo]/[main]/project data without current (8) (4).xlsx"



sheet_names = ['Electricity Demand', 'Generation Output Targets', 'Generation Capacity Targets',
               'Emissions Factor', 'Cost', 'Emissions Cap', 'Capital Expenditure Budget',
               'Dev_E', 'Dev_G', 'Dev_Q', 'Dev_C']

# Function to load data from a specific sheet
def load_data(sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)

# Streamlit app layout
st.title('Excel Data Dashboard')

# Dropdown to select a sheet
selected_sheet_name = st.selectbox('Select a sheet', sheet_names)

# Load and display data for the selected sheet
if selected_sheet_name:
    df = load_data(selected_sheet_name)
    st.write(f"### Data from the '{selected_sheet_name}' Sheet", df)


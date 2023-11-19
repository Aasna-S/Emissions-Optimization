import streamlit as st
import pandas as pd

# Path to the Excel file
from urllib.parse import quote

# Set page config
st.set_page_config(page_title="Canada Net Zero", page_icon="🌍", layout="wide")
nuc=9590000000.0*2

# Preparing the data for all the years in separate dataframes as per the provided data
def create_dataframe_from_model_results():
  data_2025 = {
        'Year': [2025] * 8,
        'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal'],
        'Generation': [60429.05, 11707.13, 401733.6, 78278.04, 87486.85, 8281.2, 1355.5, 3044.54],
        'Emissions': [0.0, 0.0, 0.0, 0.0, 32.3701345, 0.0, 0.501535, 2.3138504],
        'Cost': [129207.58183850002, 19015.305902499997, 3123880.4735999997, 1006592.9719679998, 
                 130569.74928250001, 96019.520256, 2023.015975, 11645.3655],
        'Capacity': [18.24, 7.306, 84.912, 12.105, 31.54, 2.583, 3.674, 2.929]
    }
  df_2025 = pd.DataFrame(data_2025)
  data_2030 = {
        'Year': [2030] * 8,
        'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal'],
        'Generation': [92547.75, 15214.42, 443103.1, 87724.81, 77098.86, 7526.04, 969.57, 0.0],
        'Emissions': [0.0, 0.0, 0.0, 0.0, 28.5265782, 0.0, 0.35874090000000003, 0.0],
        'Cost': [201840.1644075, 22240.8955886, 3721215.282048, 1590579.7607707, 109313.0766738, 
                 76791.8738796, 1374.6854331, 0.0],
        'Capacity': [25.212, 9.496, 88.077, 11.105, 39.714, 2.583, 3.493, 0.0]
    }
    
  df_2030 = pd.DataFrame(data_2030)
  data_2035 = {
        'Year': [2035] * 8,
        'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal'],
        'Generation': [184305.21, 42161.81, 465887.5, 131692.29, 1340.0174999999945, 19716.07, 0.0, 0.0],
        'Emissions': [0.0, 0.0, 0.0, 0.0, 0.49580647499999797, 0.0, 0.0, 0.0],
        'Cost': [401956.76164529996, 55469.763708399994, 4225567.012875, 3366763.4369202005, 
                 1804.9231714499927, 158926.5084132, 0.0, 0.0],
        'Capacity': [50.706, 25.045, 92.082, 18.559, 38.391, 4.033, 0.0, 0.0]
    }
  df_2035 = pd.DataFrame(data_2035)
  # Combine all data into one DataFrame
  return pd.concat([df_2025, df_2030, df_2035], ignore_index=True)


df = create_dataframe_from_model_results()

# Dashboard layout
st.title("Canada Net Zero Power Generation Dashboard")

# Tab layout
tab1, tab2, tab3 = st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis"])

with tab1:
    st.header("Generation Overview by Technology and Year")
    fig1 = px.bar(df, x='Year', y='Generation', color='Technology', barmode='group')
    st.plotly_chart(fig1)

# Tab 2: Emissions Analysis
with tab2:
    st.header("Emissions by Technology and Year")
    fig2 = px.bar(df, x='Year', y='Emissions', color='Technology', barmode='group')
    st.plotly_chart(fig2)

# Tab 3: Cost Analysis
with tab3:
    st.header("Cost Analysis by Technology and Year")
    fig3 = px.bar(df, x='Year', y='Cost', color='Technology', barmode='group')
    st.plotly_chart(fig3)

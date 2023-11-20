import streamlit as st
import plotly.express as px
import pandas as pd

# Set page config
st.set_page_config(page_title="Canada Net Zero", page_icon="🌍", layout="wide")
nuc=9590000000.0*2

# Preparing the data for all the years in separate dataframes as per the provided data
def create_dataframe_from_model_results():
  data_2025 = {
    'wind': {'Generation': 60429.05, 'Capacity': 64389.48, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'solar': {'Generation': 11707.13, 'Capacity': 12184.92, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'hydro': {'Generation': 401733.6, 'Capacity': 401733.6, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'nuclear': {'Generation': 140757.76, 'Capacity': 140757.76, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'natural_gas': {'Generation': 45137.17, 'Capacity': 106529.07, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'geothermal': {'Generation': 8281.2, 'Capacity': 8281.2, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'oil': {'Generation': 0.0, 'Capacity': 1379.91, 'Emissions': 35.19, 'Cost': 46757597101.6181},
    'coal': {'Generation': 0.0, 'Capacity': 8184.54, 'Emissions': 35.19, 'Cost': 46757597101.6181}
}
  df_2025 = pd.DataFrame(data_2025)
  data_2030 = {
    'wind': {'Generation': 92547.75, 'Capacity': 193168.44, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'solar': {'Generation': 15214.42, 'Capacity': 36554.76, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'hydro': {'Generation': 443103.1, 'Capacity': 443103.1, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'nuclear': {'Generation': 192045.74, 'Capacity': 192045.74, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'natural_gas': {'Generation': 19591.28, 'Capacity': 106529.07, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'geothermal': {'Generation': 7526.04, 'Capacity': 8281.2, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'oil': {'Generation': 0.0, 'Capacity': 0.0, 'Emissions': 24.89, 'Cost': 56348716040.62008},
    'coal': {'Generation': 0.0, 'Capacity': 0.0, 'Emissions': 24.89, 'Cost': 56348716040.62008}
}

    
  df_2030 = pd.DataFrame(data_2030)
  data_2035 = {
    'wind': {'Generation': 184000.0, 'Capacity': 321947.4, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'solar': {'Generation': 42000.0, 'Capacity': 60924.6, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'hydro': {'Generation': 460000.0, 'Capacity': 460000.0, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'nuclear': {'Generation': 200355.62, 'Capacity': 200355.62, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'natural_gas': {'Generation': 0.0, 'Capacity': 106529.07, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'geothermal': {'Generation': 0.0, 'Capacity': 8281.2, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'oil': {'Generation': 0.0, 'Capacity': 0.0, 'Emissions': 18.07326744, 'Cost': 69704387961.0},
    'coal': {'Generation': 0.0, 'Capacity': 0.0, 'Emissions': 18.07326744, 'Cost': 69704387961.0}
}
  df_2035 = pd.DataFrame(data_2035)
  # Combine all data into one DataFrame
  return pd.concat([df_2025, df_2030, df_2035], ignore_index=True)


df = create_dataframe_from_model_results()

# Dashboard layout
st.title("Canada Net Zero Power Generation")

# Layout using tabs
tab1, tab2, tab3 = st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis"])

# Layout using tabs
tab1, tab2, tab3 = st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis"])

# Tab 1: Generation Overview
with tab1:
    st.header("Generation Overview by Technology and Year")
    fig1 = px.bar(df, x='Year', y='Generation', color='Technology', barmode='group')
    st.plotly_chart(fig1)

    # Interactive Line Chart
    st.subheader("Interactive Line Chart for Energy Generation")
    selected_tech = st.selectbox("Select Technology", df['Technology'].unique())
    filtered_data = df[df['Technology'] == selected_tech]
    fig_line = px.line(filtered_data, x="Year", y="Generation", title=f"Generation Over Time for {selected_tech}")
    st.plotly_chart(fig_line)

# Tab 2: Emissions Analysis
with tab2:
    st.header("Emissions by Technology and Year")
    fig2 = px.bar(df, x='Year', y='Emissions', color='Technology', barmode='group')
    st.plotly_chart(fig2)

    # Comparison Chart
    st.subheader("Comparison of Technologies")
    year_to_compare = st.select_slider("Select Year", options=df['Year'].unique(), value=df['Year'].max())
    compare_data = df[df['Year'] == year_to_compare]
    fig_compare = px.bar(compare_data, x='Technology', y='Generation', title=f"Generation Comparison for {year_to_compare}")
    st.plotly_chart(fig_compare)

# Tab 3: Cost Analysis
with tab3:
    st.header("Cost Analysis by Technology and Year")
    fig3 = px.bar(df, x='Year', y='Cost', color='Technology', barmode='group')
    st.plotly_chart(fig3)

    # Data Table
    st.subheader("Detailed Data Table")
    st.dataframe(df)

# Add more widgets or visualizations as needed

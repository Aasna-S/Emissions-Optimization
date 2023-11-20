import streamlit as st
import plotly.express as px
import pandas as pd

# Set page config
st.set_page_config(page_title="Canada Net Zero", page_icon="🌍", layout="wide")

# Create a DataFrame from model results
def create_dataframe_from_model_results():
    data = {
        'Year': [2025]*8 + [2030]*8 + [2035]*8,
        'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal']*3,
        'Generation': [60429.05, 11707.13, 401733.6, 140757.76, 45137.17, 8281.2, 0.0, 0.0,
                       92547.75, 15214.42, 443103.1, 192045.74, 19591.28, 7526.04, 0.0, 0.0,
                       184000.0, 42000.0, 460000.0, 200355.62, 0.0, 0.0, 0.0, 0.0],
        'Capacity': [64389.48, 12184.92, 401733.6, 140757.76, 106529.07, 8281.2, 1379.91, 8184.54,
                     193168.44, 36554.76, 443103.1, 192045.74, 106529.07, 8281.2, 0.0, 0.0,
                     321947.4, 60924.6, 460000.0, 200355.62, 106529.07, 8281.2, 0.0, 0.0],
        'Emissions': [35.19]*8 + [24.89]*8 + [18.07]*8,
        'Cost': [46757597101.6181]*8 + [56348716040.62008]*8 + [69704387961.0]*8
    }
    return pd.DataFrame(data)

df = create_dataframe_from_model_results()

# Dashboard layout
st.title("Canada Net Zero Power Generation Dashboard")

# Layout using tabs
tab1, tab2, tab3 = st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis"])

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

with tab3:
    st.header("Cost Analysis by Technology and Year")
    fig3 = px.bar(df, x='Year', y='Cost', color='Technology', barmode='group')
    st.plotly_chart(fig3)

    # Data Table
    st.subheader("Detailed Data Table")
    st.dataframe(df)

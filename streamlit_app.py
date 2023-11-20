import streamlit as st
import plotly.express as px
import pandas as pd

# Set page config
st.set_page_config(page_title="Canada Net Zero", page_icon="🌍", layout="wide")

@st.cache
# Create a DataFrame from model results
def create_dataframe_from_model_results():
    data = {
    'Year': [2025]*8 + [2030]*8 + [2035]*8,
    'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal']*3,
    'Generation': [
        60429.05, 7022.27, 401733.6, 61714.80, 87486.85, 14835.78, 17267.87, 17555.67,
        92547.75, 15214.42, 443103.1, 192045.74, 19591.28, 7526.04, 0.0, 0.0,
        384355.62, 42000.0, 460000.0, 200355.62, 0.0, 0.0, 0.0, 0.0
    ],
    'Capacity': [
        64389.48, 12184.92, 401733.6, 78631.37, 106529.07, 14835.78, 17267.87, 17555.67,
        193168.44, 36554.76, 443103.1, 192045.74, 106529.07, 8281.2, 0.0, 0.0,
        384355.62, 60924.6, 460000.0, 200355.62, 106529.07, 8281.2, 0.0, 0.0
    ],
    'Emissions': [
        0.9064357500000001, 0.31249102456246486, 9.641606399999999, 1.689093156527198, 
         42.868556500000004, 0.5637597214768317, 8.461260013019402, 14.395653940518045, 
        1.38821625, 0.6770416899999999, 10.6344744, 2.3045488282845183, 
        9.599729311715484, 0.28598952, 0.0, 0.0, 
        5.765, 1.869, 11.04, 2.40426744, 0.0, 0.0, 0.0, 0.0
    ],
    'Cost': [
        3441403582.340755, 46757597101.6181, 23323799910.84075, 4052626813.89698, 
        1193777129.8407576, 46757597101.6181, 46757597101.6181, 46757597101.6181, 
        8350474995.253318, 3996403672.7533255, 28187146477.753326, 17971513125.981358, 
        1460321671.845374, 1601898273.5533285, 869840362.7533255, 56348716040.62008, 
        32312707010.675564, 9876242246.075558, 29604242246.07553, 1245242246.0755577, 
        69704387961.0, 1245242246.0755577, 69704387961.0, 69704387961.0
    ]
}
    return pd.DataFrame(data)

df = create_dataframe_from_model_results()

# Dashboard layout
st.title("Canada Net Zero Power Generation")

# Layout using tabs
tab1, tab2, tab3 = st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis"])

with tab1:
    st.header("Generation Overview by Technology and Year")
    year_options = ['All'] + sorted(df['Year'].unique().tolist())
    year_filter = st.selectbox("Select the Year", options=year_options)
    if year_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Year'] == year_filter]
    # KPIs
    total_emission = total_emission = filtered_df['Emissions'].sum()
    total_cost = filtered_df['Cost'].sum()
    
    # Layout using containers and columns
    kpi1, kpi2 = st.columns(2)
    kpi1.metric("Total Emissions", f"{total_emission:.2f}",delta=None, delta_color="inverse")
    kpi2.metric("Total Cost", f"${total_cost:,.2f}",delta=None, delta_color="inverse")
    # Charts layout 
    chart1, chart2 = st.columns(2)
    with chart1:
        fig1 = px.bar(df, x='Year', y='Generation', color='Technology', barmode='group')
        st.plotly_chart(fig1)

    with chart2: 
        # Interactive Line Chart
        st.subheader("Interactive Line Chart for Energy Generation")
        selected_tech = st.selectbox("Select Technology", df['Technology'].unique())
        filtered_data = df[df['Technology'] == selected_tech]
        fig_line = px.line(filtered_data, x="Year", y="Generation", title=f"Generation Over Time for {selected_tech}")
        st.plotly_chart(fig_line)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Cost by Source")
        fig3 = px.bar(filtered_df.sort_values('Cost (CAD)', ascending=False), x='Source', y='Cost (CAD)', color='Source')
        #fig3.update_layout(showlegend=False)
        st.plotly_chart(fig3)
    with col2:
        st.markdown("### Detailed Data View")
        st.dataframe(filtered_df)

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

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
    ],

    'Positive Generation Deviation': [2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 
    ],
    'Negative Generation Deviation':[0.0,0.0,0.0,0.0,15670.52,0.0,0.0,0.0,
                                     0.0,0.0,0.0,0.0,26302.94,0.0,969.57,0.0,
                                     305.20,161.80,5887.5,0.0,41866.65,19716.07,726.09,0.0
                                    
    ],
    'Positive Capacity Deviation':[2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ],
    'Negative Capacity Deviation': [2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ],
    'Positive Emissions Deviation': [2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ],
    'Negative Emissions Deviation': [2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ],
    'Positive Cost Deviation': [2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ],
    'Negative Cost Deviation':[2285570.95,779079.38,1064516.4, 2854221.95,0.0,917771.43,70460.82,39870.09,
                                      1566785.58, 544111.42,593980.23,1986441.85,0.0, 647473.96,0.0,0.0,
                                      0.0,0.0,0.0,68663.33,0.0,0.0,0.0,0.0 ]
}
    return pd.DataFrame(data)

df = create_dataframe_from_model_results()

# Dashboard layout
st.title("Canada Power Generation Insights (Goal Programming Model)")

# Canada-specific narrative
st.write("This dashboard provides an in-depth analysis of power generation in Canada, focusing on emissions, costs, and technology trends. Explore the data and gain insights into Canada's journey towards a sustainable and net-zero emissions future. The results presented here are based on a goal programming model.")

# Create tabs for different sections
tab1, tab2, tab3, tab4= st.tabs(["Generation Overview", "Emissions Analysis", "Cost Analysis", "Capacity Analysis"])

with tab1:
    st.header("Power Generation Overview")
    st.markdown("Explore power generation data and its impact on emissions reduction.")
    year_options = ['All'] + sorted(df['Year'].unique().tolist())
    year_filter = st.selectbox("Select the Year", options=year_options, key="gen_year_select")
    if year_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Year'] == year_filter]
    
    # KPIs
    total_emission = filtered_df['Emissions'].sum()
    total_cost = filtered_df['Cost'].sum()
    
    # Layout using containers and columns
    kpi1, kpi2 = st.columns(2)
    kpi1.metric("Total Emissions", f"{total_emission:.2f}", delta=None, delta_color="inverse")
    kpi2.metric("Total Cost", f"${total_cost:,.2f}", delta=None, delta_color="inverse")

    chart_container, table_container = st.columns([2,1])
    with chart_container:
        st.markdown("### Generation by Source")
        #fig1 = px.bar(filtered_df, x='Year', y='Generation', color='Technology', barmode='group')
        #st.plotly_chart(fig1, height=300, width = 400)  # Adjust height as needed
        fig_generation_deviation = px.bar(filtered_data, x='Year', y='Generation', color='Technology', barmode='group',
                                  title=f"Generation Overview with Deviations for {selected_tech}")
        # Add lines for positive and negative deviations
        fig_generation_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Positive Generation Deviation'],
                                             mode='lines', name='Positive Deviation'))
        fig_generation_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Negative Generation Deviation'],
                                             mode='lines', name='Negative Deviation'))

        st.plotly_chart(fig_generation_deviation)
    with table_container:
        st.subheader("Detailed Data Overview")
        st.dataframe(filtered_df, height=300)  # Adjust height as needed

    st.subheader("Interactive Line Chart for Energy Generation")
    selected_tech = st.selectbox("Select Technology", df['Technology'].unique(), key="gen_tech_select")
    filtered_data = df[df['Technology'] == selected_tech]
    fig_line = px.line(filtered_data, x="Year", y="Generation", title=f"Generation Over Time for {selected_tech}")
    st.plotly_chart(fig_line)

with tab2:
    st.header("Emissions Overview")
    st.markdown("Explore greenhouse gas emissions data in relation to power generation.")
    year_options = ['All'] + sorted(df['Year'].unique().tolist())
    year_filter = st.selectbox("Select the Year", options=year_options, key="emissions_year_select")
    if year_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Year'] == year_filter]
    
    st.markdown("### Emissions by Source")
    #fig2 = px.bar(filtered_df, x='Year', y='Emissions', color='Technology', barmode='group')
    #st.plotly_chart(fig2)
    fig_emissions_deviation = px.bar(filtered_data, x='Year', y='Emissions', color='Technology', barmode='group',
                                  title=f"Emissions Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    fig_emissions_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Positive Emissions Deviation'],
                                                 mode='lines', name='Positive Deviation'))
    fig_emissions_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Negative Emissions Deviation'],
                                                 mode='lines', name='Negative Deviation'))

    st.plotly_chart(fig_emissions_deviation)
    st.subheader("Emissions Over Time")
    fig_line_emissions = px.line(df, x='Year', y='Emissions', color='Technology', title="Emissions Over Time")
    st.plotly_chart(fig_line_emissions)

with tab3:
    st.header("Cost Analysis")
    st.markdown("Analyze the cost breakdown of power generation technologies.")
    year_options = ['All'] + sorted(df['Year'].unique().tolist())
    year_filter = st.selectbox("Select the Year", options=year_options, key="cost_year_select")
    if year_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Year'] == year_filter]
    
    #fig3 = px.bar(filtered_df, x='Year', y='Cost', color='Technology', barmode='group')
    #st.plotly_chart(fig3)
    fig_cost_deviation = px.bar(filtered_data, x='Year', y='Cost', color='Technology', barmode='group',
                            title=f"Cost Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    fig_cost_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Positive Cost Deviation'],
                                             mode='lines', name='Positive Deviation'))
    fig_cost_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Negative Cost Deviation'],
                                             mode='lines', name='Negative Deviation'))

    st.plotly_chart(fig_cost_deviation)
    st.subheader("Bar Chart for Cost Breakdown")
    selected_year = st.select_slider("Select Year", options=df['Year'].unique(), value=df['Year'].max(), key="cost_slider")
    cost_breakdown_data = df[df['Year'] == selected_year]
    fig_cost_breakdown = px.bar(cost_breakdown_data, x='Technology', y='Cost', title=f"Cost Breakdown for {selected_year}")
    st.plotly_chart(fig_cost_breakdown)
with tab4:
    st.header("Capacity Analysis")
    st.markdown("Analyze power generation capacity by source for different time periods.")
    year_options = ['All'] + sorted(df['Year'].unique().tolist())
    year_filter = st.selectbox("Select the Year", options=year_options, key="capacity_year_select")
    if year_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Year'] == year_filter]
    
    st.markdown("### Capacity by Source")
    #fig_capacity = px.bar(filtered_df, x='Year', y='Capacity', color='Technology', barmode='group')
    #st.plotly_chart(fig_capacity)
    fig_capacity_deviation = px.bar(filtered_data, x='Year', y='Capacity', color='Technology', barmode='group',
                                title=f"Capacity Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    fig_capacity_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Positive Capacity Deviation'],
                                                mode='lines', name='Positive Deviation'))
    fig_capacity_deviation.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Negative Capacity Deviation'],
                                                mode='lines', name='Negative Deviation'))
    
    st.plotly_chart(fig_capacity_deviation)
    st.subheader("Capacity Over Time")
    fig_line_capacity = px.line(df, x='Year', y='Capacity', color='Technology', title="Capacity Over Time")
    st.plotly_chart(fig_line_capacity)

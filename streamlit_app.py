import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Set page config
st.set_page_config(page_title="Canada Net Zero", page_icon="🌍", layout="wide")
# Create a DataFrame from model results
def create_dataframe_from_model_results():
    data = {
    'Year': [2025]*8 + [2030]*8 + [2035]*8,
    'Technology': ['wind', 'solar', 'hydro', 'nuclear', 'natural_gas', 'geothermal', 'oil', 'coal']*3,
    'Generation': [
        60666.67, 11685.39, 401666.67, 94391.94, 87081.63, 8157.89, 1346.94, 3048.78, # 2025
        92666.67, 15280.90, 442916.67, 133450.89, 77102.04, 7631.58, 979.59, 0.0, # 2030  
        184000.00, 42247.19, 465833.33, 134706.80, 41857.14, 16976.46, 734.69, 0.0 # 2035
    ],
    'Capacity': [
        64389.48, 12184.92, 401733.60, 94391.94, 106529.07, 8281.20, 1379.91, 8184.54, # 2025
        193168.44, 36554.76, 442916.67, 133450.89, 106529.07, 8281.20, 1379.91, 0.0, # 2030
        321947.40, 60924.60, 465833.33, 134706.80, 106529.07, 16976.46, 1379.91, 0.0 # 2035
    ],
    'Emissions': [
        0.91, 0.52, 9.64, 1.13, 42.67, 0.31, 0.66, 2.5, # 2025
        1.39, 0.68, 10.63, 1.60, 37.78, 0.29, 0.48, 0.0, # 2030
        2.76, 1.88, 11.18, 1.62, 20.51, 0.65, 0.36, 0.0 # 2035
    ], 
    'Cost': [
        4884480111.5, 2405815215.0, 24766876440.0, 6970659462.0, 2636853659.0, 805512324.0, 113279135.0, 250261188.0, # 2025
        7480634632.5, 3126563310.0, 42621342516.3, 7811894330.5, 2323759640.4, 732057910.8, 81026964.9, 0.0, # 2030 
        26910907923.6, 8664251955.0, 28721964375.0, 11727198424.5, 1261860831.0, 1917782128.9, 60679341.3, 0.0 # 2035
    ],
    'Positive Generation Deviation': [
        237.61, 21.74, 66.93, 0.0, 405.22, 123.31, 8.56, 0.0, # 2025
        0.0, 0.0, 186.43, 0.0, 0.0, 0.0, 0.0, 0.0, # 2030
        305.21, 0.0, 54.17, 0.0, 9.51, 2739.61, 0.0, 0.0 # 2035
    ],
    'Negative Generation Deviation': [
        0.0, 0.0, 0.0, 16113.90, 0.0, 0.0, 0.0, 4.24, # 2025
        118.92, 66.48, 0.0, 45726.08, 3.18, 105.54, 10.02, 0.0, # 2030
        0.0, 85.38, 0.0, 3014.51, 0.0, 0.0, 8.60, 0.0 # 2035
    ],
    'Positive Capacity Deviation': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2025 
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2030
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 # 2035
    ],
    'Negative Capacity Deviation': [
        0.0, 0.0, 0.0, 15760.57, 0.0, 0.0, 0.0, 0.0, # 2025
        0.0, 0.0, 41183.07, 54819.52, 0.0, 0.0, 0.0, 0.0, # 2030
        0.0, 0.0, 64099.73, 56075.43, 0.0, 8695.26, 0.0, 0.0 # 2035
    ],
    'Positive Emissions Deviation': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2025
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2030
        0.0, 0.0, 0.0, 0.0, 0.0, 0.105, 0.0, 0.0 # 2035
    ],
    'Negative Emissions Deviation': [
        0.0, 0.0, 0.0, 0.193, 0.0, 0.0, 0.0, 0.0, # 2025
        0.0, 0.0, 0.0, 0.551, 0.0, 0.0, 0.0, 0.0, # 2030
        0.0, 0.0, 0.0, 0.036, 0.0, 0.0, 0.0, 0.0 # 2035
    ],
    'Positive Cost Deviation': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2025
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2030
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 # 2035
    ],
    'Negative Cost Deviation': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, # 2025
        0.0, 0.0, 15304.04, 0.0, 0.0, 0.0, 0.0, 0.0, # 2030
        120135.18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 # 2035
    ]
    


    
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
    total_generation= filtered_df['Generation'].sum()
    total_capacity= filtered_df['Capacity'].sum()

    Lgst= [
    [60429.05, 92547.75, 184305.21],  # Wind
    [11707.13, 15214.42, 42161.81],   # Solar
    [401733.6, 443103.1, 465887.5],   # Hydro
    [78278.04, 87724.81, 131692.29],  # Nuclear
    [87486.85, 77098.86, 41866.65],   # Natural Gas
    [8281.2, 7526.04, 19716.07],      # Geothermal
    [1355.5, 969.57, 726.09],         # Oil
    [3044.54, 0, 0]                   # Coal
]

    # Layout using containers and columns
    kpi1, kpi2,kpi3,kpi4 = st.columns(4)
    kpi1.metric("Total Generation (GW)", f"{total_generation:.2f}", delta=None, delta_color="inverse")
    kpi2.metric("Total Emissions (MTCO2e)", f"{total_emission:.2f}", delta=None, delta_color="inverse")
    kpi3.metric("Total Cost (CAD)", f"${total_cost:,.2f}", delta=None, delta_color="inverse")
    kpi4.metric("Total Capacity (GWh)", f"{total_capacity:.2f}", delta=None, delta_color="inverse")
    chart_container, table_container = st.columns([2,1])
    with chart_container:
        st.markdown("### Generation by Source")
        fig1 = px.bar(filtered_df, x='Year', y='Generation', color='Technology', barmode='group')
        st.plotly_chart(fig1, height=300, width = 400)  # Adjust height as needed
        # Add goal markers 
    fig1.add_scatter(
    x=['wind','solar','hydro','nuclear','natural_gas','geothermal','oil','coal'],
    y=[Lgst[0][0], Lgst[1][0], Lgst[2][0], Lgst[3][0], Lgst[4][0], Lgst[5][0], Lgst[6][0], Lgst[7][0]], 
    mode='markers',
    marker=dict(color='black',size=12)
        )

# Add deviation shapes
    for i in range(len(df)):
        fig1.add_shape(
            type='line',
            x0=df.loc[i,'Technology'], 
            x1=df.loc[i,'Technology'],
            y0=df.loc[i,'Generation'] - df.loc[i,'Negative Generation Deviation'],
            y1=df.loc[i,'Generation'] + df.loc[i,'Positive Generation Deviation'],
            line=dict(color='red', width=2, dash='dash') 
        )

    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1) 
        #fig_generation_deviation = px.bar(filtered_df, x='Year', y='Generation', color='Technology', barmode='group',
                                  #title=f"Generation Overview with Deviations")
        # Add lines for positive and negative deviations
        #fig_generation_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Positive Generation Deviation'],
                                   #          mode='lines', name='Positive Deviation'))
        #fig_generation_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Negative Generation Deviation'],
                                    #         mode='lines', name='Negative Deviation'))

        #st.plotly_chart(fig_generation_deviation)
    with table_container:
        st.subheader("Detailed Data Overview")
        st.dataframe(filtered_df, height=300)  # Adjust height as needed

    st.subheader("Energy Generation Over time")
    fig_line = px.line(df, x="Year", y="Generation", title=f" Energy Generation Over Time", color = 'Technology')
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
    # KPIs
    total_emission = filtered_df['Emissions'].sum()
    total_cost = filtered_df['Cost'].sum()
    total_generation= filtered_df['Generation'].sum()
    total_capacity= filtered_df['Capacity'].sum()
    
    # Layout using containers and columns
    kpi1, kpi2,kpi3,kpi4 = st.columns(4)
    kpi1.metric("Total Generation (GW)", f"{total_generation:.2f}", delta=None, delta_color="inverse")
    kpi2.metric("Total Emissions (MTCO2e)", f"{total_emission:.2f}", delta=None, delta_color="inverse")
    kpi3.metric("Total Cost (CAD)", f"${total_cost:,.2f}", delta=None, delta_color="inverse")
    kpi4.metric("Total Capacity (GWh)", f"{total_capacity:.2f}", delta=None, delta_color="inverse")
    
    
    st.markdown("### Emissions by Source")
    fig2 = px.bar(filtered_df, x='Year', y='Emissions', color='Technology', barmode='group')
    st.plotly_chart(fig2)
    #fig_emissions_deviation = px.bar(filtered_df, x='Year', y='Emissions', color='Technology', barmode='group',
                                #  title=f"Emissions Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    #fig_emissions_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Positive Emissions Deviation'],
                                 #                mode='lines', name='Positive Deviation'))
    #fig_emissions_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Negative Emissions Deviation'],
                                   #              mode='lines', name='Negative Deviation'))
    #st.plotly_chart(fig_emissions_deviation)
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
    # KPIs
    total_emission = filtered_df['Emissions'].sum()
    total_cost = filtered_df['Cost'].sum()
    total_generation= filtered_df['Generation'].sum()
    total_capacity= filtered_df['Capacity'].sum()
    
    # Layout using containers and columns
    kpi1, kpi2,kpi3,kpi4 = st.columns(4)
    kpi1.metric("Total Generation (GW)", f"{total_generation:.2f}", delta=None, delta_color="inverse")
    kpi2.metric("Total Emissions (MTCO2e)", f"{total_emission:.2f}", delta=None, delta_color="inverse")
    kpi3.metric("Total Cost (CAD)", f"${total_cost:,.2f}", delta=None, delta_color="inverse")
    kpi4.metric("Total Capacity (GWh)", f"{total_capacity:.2f}", delta=None, delta_color="inverse")
    
    fig3 = px.bar(filtered_df, x='Year', y='Cost', color='Technology', barmode='group')
    st.plotly_chart(fig3)
    #fig_cost_deviation = px.bar(filtered_df, x='Year', y='Cost', color='Technology', barmode='group',
                           # title=f"Cost Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    #fig_cost_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Positive Cost Deviation'],
                            #                 mode='lines', name='Positive Deviation'))
    #fig_cost_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Negative Cost Deviation'],
                             #                mode='lines', name='Negative Deviation'))

    #st.plotly_chart(fig_cost_deviation)
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
    # KPIs
    total_emission = filtered_df['Emissions'].sum()
    total_cost = filtered_df['Cost'].sum()
    total_generation= filtered_df['Generation'].sum()
    total_capacity= filtered_df['Capacity'].sum()
    
    # Layout using containers and columns
    kpi1, kpi2,kpi3,kpi4 = st.columns(4)
    kpi1.metric("Total Generation (GW)", f"{total_generation:.2f}", delta=None, delta_color="inverse")
    kpi2.metric("Total Emissions (MTCO2e)", f"{total_emission:.2f}", delta=None, delta_color="inverse")
    kpi3.metric("Total Cost (CAD)", f"${total_cost:,.2f}", delta=None, delta_color="inverse")
    kpi4.metric("Total Capacity (GWh)", f"{total_capacity:.2f}", delta=None, delta_color="inverse")
    
    
    
    st.markdown("### Capacity by Source")
    fig_capacity = px.bar(filtered_df, x='Year', y='Capacity', color='Technology', barmode='group')
    st.plotly_chart(fig_capacity)
    #fig_capacity_deviation = px.bar(filtered_df, x='Year', y='Capacity', color='Technology', barmode='group',
    #                           title=f"Capacity Analysis with Deviations for {selected_tech}")

    # Add lines for positive and negative deviations
    #fig_capacity_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Positive Capacity Deviation'],
    #                                            mode='lines', name='Positive Deviation'))
    #fig_capacity_deviation.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df['Negative Capacity Deviation'],
     #                                           mode='lines', name='Negative Deviation'))
    
    #st.plotly_chart(fig_capacity_deviation)
    st.subheader("Capacity Over Time")
    fig_line_capacity = px.line(df, x='Year', y='Capacity', color='Technology', title="Capacity Over Time")
    st.plotly_chart(fig_line_capacity)

import streamlit as st
import pandas as pd

def show_overview_kpis(df_filtered: pd.DataFrame):
    st.header("2. Network Performance (Filtered Selection)")

    col1, col2, col3 = st.columns(3)
    
    # Calculate KPIs based only on filtered data
    kpi_bikes = df_filtered['velos_dispo'].sum()
    kpi_docks = df_filtered['bornes_libres'].sum()
    kpi_capacity = df_filtered['capacite'].sum()

    kpi_filling_rate = kpi_bikes / kpi_capacity if kpi_capacity > 0 else 0 

    # Display KPIs
    col1.metric("Available Bikes (Selection)", f"{kpi_bikes:,.0f}")
    col2.metric("Free Docks (Selection)", f"{kpi_docks:,.0f}")
    col3.metric("Filling Rate (Selection)", f"{kpi_filling_rate:.1%}")
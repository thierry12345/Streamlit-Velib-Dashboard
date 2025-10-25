import streamlit as st
import pandas as pd
from utilitaire.io import load_data
from utilitaire.prep import make_tables
from sections.intro import show_intro_and_quality
from sections.overview import show_overview_kpis
from sections.deep_dives import show_deep_dives
from sections.conclusions import show_conclusions

# --- Page Configuration ---
FILE_PATH = "data/velib-disponibilite-en-temps-reel_22october.csv" 
st.set_page_config(
    page_title="Vélib' Métropole: Where to Rebalance?", 
    layout="wide",
    menu_items={'About': "Data Storytelling Project - Instantaneous Vélib' Analysis"}
)

@st.cache_data(show_spinner="Calculating data tables...")
def get_data(path):
    """Loads raw data and prepares all necessary data tables."""
    df_raw = load_data(path)
    if df_raw.empty:
        return None
    tables = make_tables(df_raw)
    return tables

# 1. Data Loading and Preparation 
data_tables = get_data(FILE_PATH)


# Extracting tables from the dictionary
kpis_globaux = data_tables['kpis']
df_geo_full = data_tables['geo'] 
df_commune = data_tables['by_commune']
quality_metrics = data_tables['quality'] 

# Check for empty data after cleaning, placed here for robustness
if df_geo_full.empty:
    st.error("Filtered data is empty after initial cleaning.")
    st.stop()
    
# Retrieve timestamp 
date_instantané = df_geo_full['date_maj'].iloc[0].strftime('%d/%m/%Y à %H:%M:%S')



def select_all_communes(communes_dispo):
    """Sets the multiselect widget value to include all available communes."""
    st.session_state.communes_selectionnees = communes_dispo

def deselect_all_communes():
    """Sets the multiselect widget value to an empty list."""
    st.session_state.communes_selectionnees = []

# 2.Sidebar
with st.sidebar:
    st.header("Geographic Filters")
    st.markdown("Use these filters to target the zones and station states to analyze.")
    
    communes_dispo = sorted(df_commune['commune'].tolist())
    
    # Initialize session state for the multiselect if it doesn't exist
    if 'communes_selectionnees' not in st.session_state:
        st.session_state.communes_selectionnees = ['Paris'] 
        

    col_a, col_d = st.columns(2)
    with col_a:
        st.button(
            "Select All", 
            on_click=select_all_communes, 
            args=(communes_dispo,), # Pass the full list as an argument
            use_container_width=True
        )
    with col_d:
        st.button(
            "Deselect All", 
            on_click=deselect_all_communes,
            use_container_width=True
        )

    communes_selectionnees = st.multiselect(
        "Select Communes", 
        options=communes_dispo,
        default=st.session_state.communes_selectionnees,
        key='communes_selectionnees' 
    )
    
    etat_selectionne = st.multiselect(
        "Filter Station Status",
        options=['Full','Empty','Balanced'],
        default=['Full','Empty','Balanced']
    )

# 3. Applying Data Filtering
# Combined filtering on commune and status
df_filtered = df_geo_full[
    (df_geo_full['commune'].isin(communes_selectionnees)) & 
    (df_geo_full['etat_station'].isin(etat_selectionne))
].copy()
df_filtered.reset_index(drop=True, inplace=True) 

# 4. Displaying Report Sections

show_intro_and_quality(date_instantané, quality_metrics)

show_overview_kpis(df_filtered)

show_deep_dives(df_filtered, df_commune, communes_selectionnees)

show_conclusions(df_geo_full, date_instantané)
import streamlit as st
import pandas as pd
from utilitaire.viz import show_map, show_commune_barchart, show_type_barchart

def show_deep_dives(df_filtered: pd.DataFrame, df_commune: pd.DataFrame, communes_selectionnees: list):
    """
    Display of the three detailed analysis visualizations:
    map, comparison by commune, and bike type distribution.
    """
    show_map(df_filtered)
    show_commune_barchart(df_commune, communes_selectionnees)
    show_type_barchart(df_filtered)
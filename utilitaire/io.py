import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="Loading raw data...")
def load_data(file_path: str) -> pd.DataFrame:
    try:
        # Read the CSV file with appropriate parameters
        df = pd.read_csv(
            file_path, 
            sep=';', 
            encoding='utf-8', 
            on_bad_lines='skip' 
        )
        return df
    except FileNotFoundError:
        st.error(f"Read Error: File not found at the specified path: {file_path}.")
        return pd.DataFrame()
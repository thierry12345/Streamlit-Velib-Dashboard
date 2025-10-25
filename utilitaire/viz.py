import streamlit as st
import pandas as pd


COLOR_MAP_HEX = {
    'Full': '#ff0000', 
    'Empty': "#0000ff",       
    'Balanced': '#008000'                 
}

def hex_to_rgb_tuple(hex_color: str) -> list[int]:
    """
    Converts a hexadecimal color  into an RGB list [R, G, B]
    """
    hex_color = hex_color.lstrip('#')
    # Conversion of each component
    return [
        int(hex_color[0:2], 16), # Red
        int(hex_color[2:4], 16), # Green
        int(hex_color[4:6], 16)  # Blue
    ]

def show_map(df_filtered: pd.DataFrame):
    """
    Displays the map of critical stress zones 
    """
    st.header("3. Mapping of Stress Zones")
    
    if df_filtered.empty:
        st.warning("No station matches the selected filters.")
        return

    # 1. Create the series of hexadecimal colors
    color_series_hex = df_filtered['etat_station'].map(COLOR_MAP_HEX).fillna('#000000')

    # 2. Convert to [R, G, B] format for streamlit
    color_rgb_series = color_series_hex.apply(hex_to_rgb_tuple)

    # 3. Prepare the DataFrame for map display
    df_to_map = df_filtered.copy()
    df_to_map['color_map_rgb'] = color_rgb_series

    st.map(df_to_map,latitude='latitude',longitude='longitude',size='capacite',color='color_map_rgb')

    # Legend for map 
    st.markdown("""
    <p style='text-align: center; color: #ff0000;'><strong>Full</strong></p>
    <p style='text-align: center; color: #0000ff;'><strong>Empty</strong></p>
    <p style='text-align: center; color: #008000;'><strong>Balanced</strong></p>            
                
    """, unsafe_allow_html=True)
    st.markdown("---")

def show_commune_barchart(df_commune: pd.DataFrame, communes_selectionnees: list):
    """
    Displays the average filling rate per commune for the selection
    """
    st.header("4. Filling Rate by Commune (Selection)")

    df_commune_filtered = df_commune[
        df_commune['commune'].isin(communes_selectionnees)
    ].sort_values('taux_remplissage_commune', ascending=False)

    if df_commune_filtered.empty:
        st.warning("No commune selected.")
        return

    # Display the chart
    st.bar_chart(
        df_commune_filtered.set_index('commune')['taux_remplissage_commune']
    )
    st.info("View which communes are generally the most 'saturated' (high rate) or 'depleted' (low rate).")
    st.markdown("---")

def show_type_barchart(df_filtered: pd.DataFrame):
    """
    Displays the composition of available bikes (mechanical vs. electric) 
    """
    st.header("5. Bike Composition (Selection)")
    
    if df_filtered.empty:
        st.warning("No station matches the selected filters.")
        return

    # Sum of 'velos_meca' and 'velos_elec' columns
    df_velo_type = df_filtered[[
        'velos_meca', 'velos_elec'
    ]].sum().rename("Number of Bikes")

    st.bar_chart(df_velo_type)
    st.info("Distribution of available mechanical and electric bikes in the currently selected stations.")
    st.markdown("---")
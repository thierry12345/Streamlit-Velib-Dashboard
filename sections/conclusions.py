import streamlit as st
import pandas as pd

def show_conclusions(df_geo_full: pd.DataFrame, date_instantané: str):
    st.header("6. Conclusions: Insights and Action Tracks")
    
    # Identification of the top 3 most critical stations (for the whole network, unfiltered)
    top_vides = df_geo_full[df_geo_full['etat_station'] == 'Empty'].head(3)
    top_pleines = df_geo_full[df_geo_full['etat_station'] == 'Full'].head(3)
    
    col_ins1, col_ins2 = st.columns(2)
    
    with col_ins1:
        st.error("Top 3 Empty Stations (Priority: Deliver Bikes):")
        if top_vides.empty:
            st.write("No critical empty stations found in the dataset.")
        else:
            for index, row in top_vides.iterrows():
                st.write(f"- **{row['nom_station']}** ({row['commune']}) : Only **{row['velos_dispo']}** bike(s) available.")

    with col_ins2:
        st.warning("Top 3 Full Stations (Priority: Retrieve Bikes):")
        if top_pleines.empty:
             st.write("No critical full stations found in the dataset.")
        else:
            for index, row in top_pleines.iterrows():
                st.write(f"- **{row['nom_station']}** ({row['commune']}) : Only **{row['bornes_libres']}** free dock(s).")

    st.markdown("### Synthesis and Next Steps")
    st.success(f"""
    * **Immediate Action:** The stations listed above represent critical hotspots at the time of the snapshot ({date_instantané}) and are priority targets for rebalancing operations.
    * **Next Step (Temporal Analysis):** Future analysis should integrate more dataset to compare imbalances between multiple days (e.g., identify if the same stations are empty or full recurrently at the same time).
    """)
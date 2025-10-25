import pandas as pd
import numpy as np

def make_tables(df_raw: pd.DataFrame) -> dict:
    """
    Cleans the raw data, calculates key indicators (KPIs, station status),
    """
    total_rows_initial = len(df_raw)
    
    df = df_raw.copy()
    
    df.columns = [
        'id_station', 'nom_station', 'en_fonctionnement', 'capacite', 
        'bornes_libres', 'velos_dispo', 'velos_meca', 'velos_elec', 
        'borne_paiement', 'retour_possible', 'date_maj', 'coordonnees', 
        'commune', 'code_insee', 'horaires'
    ]
    
    df['date_maj'] = pd.to_datetime(df['date_maj'], errors='coerce', utc=True)
    
    coords = df['coordonnees'].str.split(',', expand=True)
    df['latitude'] = pd.to_numeric(coords[0], errors='coerce')
    df['longitude'] = pd.to_numeric(coords[1], errors='coerce')
    
    #Filtering out unusable stations
    df.dropna(subset=['latitude', 'longitude'], inplace=True) 
    df = df[df['en_fonctionnement'] == 'OUI'] 
    df = df[df['capacite'] > 0] 
 
    total_rows_final = len(df)
    rows_dropped = total_rows_initial - total_rows_final
    
    quality_data = {
        "Total Lignes Initiales": total_rows_initial,
        "Total Lignes Après Nettoyage": total_rows_final,
        "Lignes Supprimées (Invalides/Hors Service)": rows_dropped,
        "Pourcentage de Données Utilisables": f"{(total_rows_final / total_rows_initial) * 100:.2f}%",
    }
    
    #Calculation of Filling Rate and Status Determination
    df['taux_remplissage'] = (df['velos_dispo'] / df['capacite']).fillna(0)
    
    # Function to categorize station status
    def determine_etat(row):
        
        if row['taux_remplissage'] >= 0.9:
            return 'Full'
        elif row['taux_remplissage'] <= 0.05:
            return 'Empty'
        else:
            return 'Balanced'

    df['etat_station'] = df.apply(determine_etat, axis=1)
    
    #Global KPI Calculation
    kpis = {
        'total_bikes': df['velos_dispo'].sum(),
        'total_free_docks': df['bornes_libres'].sum(),
        'total_capacity': df['capacite'].sum(),
        'average_filling_rate': df['velos_dispo'].sum() / df['capacite'].sum() if df['capacite'].sum() > 0 else 0
    }
    
    #Creation of Output DataFrames
    
    # Table for mapping and filtering 
    geo_table = df[[
        'latitude', 'longitude', 'capacite', 'commune', 'etat_station', 
        'date_maj', 'velos_dispo', 'bornes_libres', 'nom_station',
        'velos_meca', 'velos_elec'
    ]].copy()
    
    # Table aggregated by commune
    summary_by_commune = df.groupby('commune').agg(
        total_velos=('velos_dispo', 'sum'),
        total_bornes=('bornes_libres', 'sum'),
        total_capacite=('capacite', 'sum')
    ).reset_index()
    
    # Calculate the filling rate at the commune level
    summary_by_commune['taux_remplissage_commune'] = (
        summary_by_commune['total_velos'] / summary_by_commune['total_capacite']
    )
    
    # 6. Return tables and metrics
    return {
        "kpis": kpis,
        "geo": geo_table,
        "by_commune": summary_by_commune,
        "quality": quality_data 
    }
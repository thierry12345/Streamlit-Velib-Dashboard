import streamlit as st

def show_intro_and_quality(snapshot_date: str, quality_metrics: dict):
    
    st.title("Vélib' Métropole: Instantaneous Imbalance Analysis")
    st.caption(f"Source: Vélib' Métropole Open Data | **Snapshot from {snapshot_date}**")
    st.markdown("---")

    # HOOK & CONTEXT
    st.markdown("""
    The rise of **bike-sharing** has become a backbone of modern urban mobility. While this trend offers freedom and ecological benefits, it introduces a constant operational challenge: **station imbalance**.
    Our analysis focuses on this critical point. The goal isn't to understand *why* people are moving, but **where and when the system is failing** at a specific moment in time.
    Imagine the frustration: arriving at a station, and it’s **empty**. Or worse, trying to return a bike, and the station is **full**. These moments, multiplied by thousands of users, represent a service failure.
    By studying a **real-time photograph** of the Vélib' network, we transform raw data into a decision-support tool designed to answer one crucial question: **Where should rebalancing teams go NOW?**
    """)

    st.header("1. Snapshot Quality and Reliability")
    st.markdown("Data validation before analysis. Out-of-service stations or stations without coordinates are excluded.")

    col_q1, col_q2, col_q3, col_q4 = st.columns(4)

    col_q1.metric("Raw Rows", quality_metrics.get("Total Lignes Initiales", 0))
    col_q2.metric("Valid Rows", quality_metrics.get("Total Lignes Après Nettoyage", 0))
    col_q3.metric("Rejected Rows", quality_metrics.get("Lignes Supprimées (Invalides/Hors Service)", 0))
    col_q4.metric("Dataset Reliability", quality_metrics.get("Pourcentage de Données Utilisables", "0.0%"))
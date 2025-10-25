# Vélib' Métropole: Where to rebalance?  
This project is a Streamlit Data Storytelling application built to help Vélib' Métropole operations teams efficiently identify and respond to real-time bike and dock imbalances across the network. The dashboard uses an instantaneous snapshot of station availability data to diagnose stress points and guide rebalancing logistics.



Context: Data quality and reliability.  
Diagnosis: Global health check and filtering for problem areas.  
Action: Precise location and required fleet composition for immediate deployment.
Implications: Identifying critical long-term stress points.

# Local setup and run instructions:  
To run this application on your local machine, follow these steps:

1. Prerequisites
Python 3.8+ installed.
The required libraries are listed in requirements.txt.


2. Installation
Clone the repository:
git clone https://github.com/thierry12345/Streamlit-Velib-Dashboard  
cd Streamlit_Project  
Install dependencies:
pip install -r requirements.txt


4. Run the app :Execute the following command in your terminal from the project root directory: streamlit run app.py

    The application will automatically open in your default web browser.



5. Data and technical details:
Dataset: Real-time Vélib' station availability data (snapshot from October 22nd).
Key Filters: Geographical area (Commune) and Station Status (Full, Empty, Balanced).
Technology Stack: Python, Pandas for data processing, Streamlit for the web application and visualization.

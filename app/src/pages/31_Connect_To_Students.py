import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Add sidebar navigation links
SideBarLinks()

# Page Title
st.title("My Student Connections")

if 'user_id' not in st.session_state:
    st.error('You must be logged in to view your connections.')
else:
    alumn_id = st.session_state['user_id']
    
    st.subheader("Your Current Student Connections")

    response = requests.get(f"http://web-api:4000/advisor/studentalumn/{alumn_id}")
    if response.status_code == 200:
        connections = response.json()
        if connections:
            # Convert to DataFrame
            df = pd.DataFrame(connections)
            # Map columns in the correct order based on the actual data
            # Reorder columns for display
            df = df[['firstName', 'lastName', 'email', 'company', 'city']]
            st.table(df)
        else:
            st.info("You don't have any student connections yet.")
    else:
        error_message = response.json().get("error", "Unknown error")
        st.error(f"Failed to retrieve connections: {error_message}")
 
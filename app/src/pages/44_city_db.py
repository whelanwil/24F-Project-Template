import logging
import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

def fetch_cities():
    """Fetch and format listings data"""
    response = requests.get(f"http://web-api:4000/apartment")
    if response.status_code == 200:
        response_data = response.json()
        if 'data' in response_data and response_data['data']:
            df = pd.DataFrame(response_data['city'])
            
            return df
    return None

# Check the role of the user
if "role" not in st.session_state:
    st.error("You do not have permission to access this page.")

else:
    role = st.session_state["role"]

    # If the user is a system administrator
    if role in ["administrator"]:
        st.title("Remove City from Database")

        df = fetch_cities()

        housing_id = st.selectbox("Select City to Remove", df['city'].tolist())
        if st.button("Remove Selected City", type="secondary"):
            delete_url = f"http://web-api:/systemAdministrator/student/{city}"
            response = requests.delete(delete_url)
                    
            if response.status_code == 200:
                st.success("City removed successfully!")
                st.rerun()
            
            else:
                st.error(f"Failed to remove city. Status code: {response.status_code}")
                st.write(f"Error details: {response.text}")
import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

st.title("Search Alumni Housing")
city = st.text_input("Enter the city to search for alumni housing:")

if st.button('Search', use_container_width=True):
    if city:
        # Making a GET request to the API to fetch alumni housing data for the specified city
        api_url = f"http://web-api:4000/advisor/alumni/{city}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            housing_data = response.json()

            if "data" in housing_data and housing_data["data"]:
                st.write(f"**Found {len(housing_data['data'])} alumni offering housing in {city}:**")
                
                # Create a DataFrame from the response data
                df = pd.DataFrame(housing_data["data"])
                st.table(df.reset_index(drop=True))
            else:
                st.write(f"No alumni found offering housing in {city}.")
        else:
            st.error(f"Error: Received status code {response.status_code}")
            st.write(response.text)
    else:
        st.warning("Please enter a city to search for alumni housing.")


        
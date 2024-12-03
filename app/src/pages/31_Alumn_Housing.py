import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

# Title and Input for city
st.title("Search Alumni Housing")
city = st.text_input("Enter the city to search for alumni housing:")

# Button to search
if st.button('Search', use_container_width=True):
    if city:

        # Making a GET request to the API to fetch alumni housing data for the specified city
        api_url = f"http://web-api:4000/alumni/{city}"  # Correct URL as per your Docker config
        response = requests.get(api_url)
        st.write(response.status_code)
        st.write(response.text)
        
        housing_data = response.json()
        
        if response.status_code == 200:
            housing_data = response.json()
            if housing_data:
                st.write(f"**Found {len(housing_data)} alumni offering housing in {city}:**")
                for alum in housing_data:
                    st.write(f"**Alumni ID:** {alum['alumID']}")
            else:
                st.write(f"No alumni found offering housing in {city}.")
        else:
            st.write(f"Error: Received status code {response.status_code}")

else:
        st.write("Please enter a city to search for alumni housing.")

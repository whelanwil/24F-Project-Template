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
        try:
            # Making a GET request to the API to fetch alumni housing data for the specified city
            api_url = f"http://localhost:4000/alumni/{city}"  # Correct URL as per your Docker config
            response = requests.get(api_url)

            if response.status_code == 200:
                housing_data = response.json()
                
                if housing_data:
                    st.write(f"**Found {len(housing_data)} alumni offering housing in {city}:**")
                    for alum in housing_data:
                        st.write(f"**Alumni ID:** {alum['alumID']}")  # Displaying alumID or other housing info
                        # You can add more details from the response here based on your API response format
                else:
                    st.write(f"No alumni found offering housing in {city}.")
            else:
                st.write(f"Failed to fetch data. Error: {response.status_code}")
        except Exception as e:
            logger.error(f"Error while fetching alumni housing data: {e}")
            st.write("An error occurred while fetching the data.")
    else:
        st.write("Please enter a city to search for alumni housing.")

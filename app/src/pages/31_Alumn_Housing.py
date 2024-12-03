import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import logging
import streamlit as st
import requests

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
            # API call to get housing data based on city
            response = requests.get(f'http://yourapiurl.com/alumni/{city}')
            housing_data = response.json()

            if housing_data:
                st.write(f"**Found {len(housing_data)} alumni offering housing in {city}:**")
                for alum in housing_data:
                    st.write(f"**Alumni ID:** {alum['alumID']}")
            else:
                st.write("No alumni found offering housing in this city.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a city.")




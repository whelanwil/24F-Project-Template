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

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Alumni Housing", "Available Apartments", "Students", "Alumni"])

with tab1:
    city = st.text_input("Enter the city to search for alumni housing:")
    if st.button('Search Alumni Housing', use_container_width=True):
        if city:
            api_url = f"http://web-api:4000/advisor/alumni/{city}"
            response = requests.get(api_url)
            
            if response.status_code == 200:
                housing_data = response.json()
                if "data" in housing_data and housing_data["data"]:
                    st.write(f"**Found {len(housing_data['data'])} alumni offering housing in {city}:**")
                    df = pd.DataFrame(housing_data["data"])
                    st.table(df.reset_index(drop=True))
                else:
                    st.info(f"No alumni found offering housing in {city}.")
            else:
                st.error(f"Error: Received status code {response.status_code}")
        else:
            st.warning("Please enter a city to search.")

with tab2:
    if city:
        api_url = f"http://web-api:4000/student/apartment/city/{city}"
        response = requests.get(api_url)
        if response.status_code == 200:
            apartments = response.json()
            if apartments:
                st.write(f"**Found {len(apartments)} available apartments in {city}:**")
                df = pd.DataFrame(apartments)
                df = df[['firstName', 'lastName', 'email', 'city', 'state', 'rent', 'beds', 'baths', 'dateAvailableFrom', 'dateAvailableTo']]
                st.table(df)
            else:
                st.info(f"No available apartments found in {city}.")
    else:
        st.warning("Please enter a city to search.")

with tab3:
    if city:
        api_url = f"http://web-api:4000/student/student/city/{city}"
        response = requests.get(api_url)
            
        if response.status_code == 200:
            students = response.json()
            if students:
                st.write(f"**Found {len(students)} students in {city}:**")
                df = pd.DataFrame(students)
                # Reorder columns for display
                df = df[['firstName', 'lastName', 'email', 'company']]
                st.table(df)
            else:
                st.info(f"No students found in {city}.")
    else:
        st.warning("Please enter a city to search.")

with tab4:
    if city:
        api_url = f"http://web-api:4000/student/alumni/city/{city}"
        response = requests.get(api_url)
        if response.status_code == 200:
            alumni = response.json()
            if alumni:
                st.write(f"**Found {len(alumni)} alumni in {city}:**")
                df = pd.DataFrame(alumni)
                # Reorder columns for display
                df = df[['firstName', 'lastName', 'email', 'company']]
                st.table(df)
            else:
                st.info(f"No alumni found in {city}.")
        else:
            st.error(f"Error: Received status code {response.status_code}")
    else:
        st.warning("Please enter a city to search.")



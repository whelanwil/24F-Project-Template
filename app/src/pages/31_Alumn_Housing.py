import logging
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

# Check the role of the user
if "role" not in st.session_state:
    st.error("You do not have permission to access this page.")
else:
    role = st.session_state["role"]

    # If the user is an advisor or student
    if role in ["advisor", "student"]:
        st.title("Search Alumni Housing")
        city = st.text_input("Enter the city to search for alumni housing:")

        if st.button('Search', use_container_width=True):
            if city:
                # Making a GET request to the API to fetch alumni housing data for the specified city
                api_url = f"http://web-api:4000/alumni/{city}"  # Correct URL as per your Docker config
                response = requests.get(api_url)

                if response.status_code == 200:
                    # Parse JSON response
                    housing_data = response.json()

                    if "data" in housing_data and housing_data["data"]:
                        st.write(f"**Found {len(housing_data['data'])} alumni offering housing in {city}:**")
                        
                        # Create a DataFrame from the response data
                        df = pd.DataFrame(housing_data["data"])
                        df_reset = df.reset_index(drop=True)

                        # Remove index entirely before displaying
                        st.table(df_reset)
                    else:
                        st.write(f"No alumni found offering housing in {city}.")
                else:
                    st.error(f"Error: Received status code {response.status_code}")
                    st.write(response.text)  # Optionally show raw response for debugging
            else:
                st.warning("Please enter a city to search for alumni housing.")

    # If the user is an alumni
    elif role == "alumni":
        st.title("Welcome!")
        st.write(f"Hello {st.session_state['first_name']}")

    # If the user has an unrecognized role
    else:
        st.error("Unrecognized role. Please contact the system administrator.")

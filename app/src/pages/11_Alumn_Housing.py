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
                api_url = f"http://web-api:4000/alumni/{city}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    housing_data = response.json()

                    if "data" in housing_data and housing_data["data"]:
                        st.write(f"**Found {len(housing_data['data'])} alumni offering housing in {city}:**")
                        
                        # Create a DataFrame from the response data
                        df = pd.DataFrame(housing_data["data"])
                
                        # Display the DataFrame as a static table without the index
                        st.table(df.reset_index(drop=True))
                    else:
                        st.write(f"No alumni found offering housing in {city}.")
                else:
                    st.error(f"Error: Received status code {response.status_code}")
                    st.write(response.text)
            else:
                st.warning("Please enter a city to search for alumni housing.")

    # If the user is an alumni
    elif role == "alumni":
        st.title("Manage Your Housing Listings")
        
        # Get current user's ID from session state
        alum_id = st.session_state.get('user_id')
        
        # Create tabs for different actions
        tab1, tab2, tab3 = st.tabs(["View My Listings", "Add New Listing", "Update Listing"])
        
        with tab1:
            st.subheader("Your Current Housing Listings")
            # Debug print
            st.write("Debug - user_id:", st.session_state.get('user_id'))
            
            # Fetch current listings with alumni details
            response = requests.get(f"http://web-api:4000/alumni/housing/{st.session_state['user_id']}")

            st.write("API Response:", response.text)

            st.write(response.text)
            if response.status_code == 200:
                st.write("PASSED")
                listings = response.json()
                st.write(listings)
                if listings:
                    # Create a more readable DataFrame
                    df = pd.DataFrame(listings)
                    # Rename columns for better display
                    df.columns = ['Housing ID', 'Bedrooms', 'Bathrooms', 'Monthly Rent ($)', 
                                'Description', 'Available From', 'Available To',
                                'Street', 'City', 'State', 'Country',
                                'First Name', 'Last Name', 'Email']
                    
                    # Format dates
                    df['Available From'] = pd.to_datetime(df['Available From']).dt.strftime('%Y-%m-%d')
                    df['Available To'] = pd.to_datetime(df['Available To']).dt.strftime('%Y-%m-%d')
                    
                    st.dataframe(df)
                    
                    # Delete listing option
                    housing_id = st.selectbox("Select Housing ID to Remove", 
                                           df['Housing ID'].tolist())
                    if st.button("Remove Selected Listing", type="secondary"):
                        response = requests.delete(f"http://web-api:4000/alumni/{housing_id}")
                        if response.status_code == 200:
                            st.success("Listing removed successfully!")
                            st.rerun()
                else:
                    st.info("You don't have any active listings.")
        
        with tab2:
            st.subheader("Add New Housing Listing")
            with st.form("new_listing_form"):
                beds = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
                baths = st.number_input("Number of Bathrooms", min_value=1, max_value=10)
                rent = st.number_input("Monthly Rent ($)", min_value=0)
                description = st.text_area("Description")
                date_from = st.date_input("Available From")
                date_to = st.date_input("Available To")
                street = st.text_input("Street Number")
                city = st.text_input("City")
                state = st.text_input("State")
                country = st.text_input("Country")
                
                if st.form_submit_button("Add Listing"):
                    # Format dates for API
                    date_from_str = datetime.combine(date_from, datetime.min.time()).strftime('%Y-%m-%d %H:%M:%S')
                    date_to_str = datetime.combine(date_to, datetime.min.time()).strftime('%Y-%m-%d %H:%M:%S')
                    
                    data = {
                        "alumID": alum_id,
                        "bed": beds,
                        "baths": baths,
                        "rent": rent,
                        "description": description,
                        "dateAvailableFrom": date_from_str,
                        "dateAvailableTo": date_to_str,
                        "street": street,
                        "city": city,
                        "state": state,
                        "country": country
                    }
                    
                    response = requests.post("http://web-api:4000/alumni", json=data)
                    if response.status_code == 200:
                        st.success("New listing added successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to add listing. Please try again.")
        
        with tab3:
            st.subheader("Update Existing Listing")
            # Similar form to Add New Listing but with PUT request
            # Pre-fill form with existing data if available
            with st.form("update_listing_form"):
                # Same fields as Add New Listing
                if st.form_submit_button("Update Listing"):
                    # Similar to Add New Listing but using PUT request
                    response = requests.put("http://web-api:4000/alumni")
                    if response.status_code == 200:
                        st.success("Listing updated successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to update listing. Please try again.")

    # If the user has an unrecognized role
    else:
        st.error("Unrecognized role. Please contact the system administrator.")

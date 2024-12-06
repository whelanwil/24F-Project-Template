import logging
import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

st.title("Manage Your Housing Listings")

# Get current user's ID from session state
alum_id = st.session_state.get('user_id')

# Initialize session state for active tab if not exists
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "View My Listings"

# Create tabs for different actions
tab1, tab2 = st.tabs(["View My Listings", "Add New Listing"])

# Show success message if it exists and clear it
if st.session_state.get('show_success', False):
    st.success("New listing added successfully!")
    del st.session_state.show_success

def fetch_listings(alum_id):
    """Fetch and format listings data"""
    response = requests.get(f"http://web-api:4000/alumni/alumni/housing/{alum_id}")
    if response.status_code == 200:
        response_data = response.json()
        if 'data' in response_data and response_data['data']:
            df = pd.DataFrame(response_data['data'])
            df = df[['housingID', 'beds', 'baths', 'rent', 
                    'description', 'dateAvailableFrom', 'dateAvailableTo',
                    'street', 'city', 'state', 'country',
                    'firstName', 'lastName', 'email']]
            
            # Format dates
            df['dateAvailableFrom'] = pd.to_datetime(df['dateAvailableFrom']).dt.strftime('%Y-%m-%d')
            df['dateAvailableTo'] = pd.to_datetime(df['dateAvailableTo']).dt.strftime('%Y-%m-%d')
            
            # Rename columns for display
            df.columns = ['Housing ID', 'Bedrooms', 'Bathrooms', 'Monthly Rent ($)', 
                        'Description', 'Available From', 'Available To',
                        'Street', 'City', 'State', 'Country',
                        'First Name', 'Last Name', 'Email']
            return df
    return None

with tab1:
    st.subheader("Your Current Housing Listings")
    # Debug print
    st.write("Debug - user_id:", st.session_state.get('user_id'))
    
    # Fetch and display current listings
    df = fetch_listings(alum_id)
    if df is not None:
        st.dataframe(df)
        
        # Delete listing option
        housing_id = st.selectbox("Select Housing ID to Remove", 
                                df['Housing ID'].tolist())
        if st.button("Remove Selected Listing", type="secondary"):
            delete_url = f"http://web-api:4000/alumni/alumni/{housing_id}"
            response = requests.delete(delete_url)
            
            if response.status_code == 200:
                st.success("Listing removed successfully!")
                st.rerun()
            else:
                st.error(f"Failed to remove listing. Status code: {response.status_code}")
                st.write(f"Error details: {response.text}")
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
            
            response = requests.post("http://web-api:4000/alumni/alumni", json=data)
            if response.status_code == 200:
                st.success("New listing added successfully!")
                # Store success message in session state
                st.session_state.show_success = True
                # Switch back to tab 1
                st.session_state.active_tab = "View My Listings"
                st.rerun()
            else:
                st.error(f"Failed to add listing. Status code: {response.status_code}")
                st.write(f"Error details: {response.text}")



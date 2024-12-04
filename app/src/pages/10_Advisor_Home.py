import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title(f"Welcome Co-op Advisor, {st.session_state['first_name']}!")
st.write('')
st.write('### What would you like to do today?')

# Button to search alumni housing (shared with students)
if st.button('Search Alumni Housing', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/11_Alumn_Housing.py')  # Shared page

# Button to connect with alumni or students (shared with students)
if st.button('Connect with Alumni or Students', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/33_Connect_with_Alumni.py')  # Shared page

# Button to track student housing status (advisor-specific)
if st.button('Track Student Housing Status', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/01_Student_housing_preferences.py')  # Advisor-specific page


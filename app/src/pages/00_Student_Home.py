import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}!")
st.subheader("Student Dashboard")
st.write('')
st.write('### What would you like to do today?')

if st.button('Search Alumni Housing', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Search_Alum_Housing.py')

if st.button('Update Profile Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Student_housing_preferences.py')

if st.button('Connect with Alumni', 
            type='primary', 
            use_container_width=True):
  st.switch_page('pages/02_Student_Alumni_Connection.py')

if st.button('Edit Parent Housing Relationship',
            type='primary', 
            use_container_width=True):
  st.switch_page('pages/40_parent.py')
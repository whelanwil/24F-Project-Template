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
  st.switch_page('pages/31_Alumn_Housing.py')

if st.button('Update Housing Settings (Preferences and Status)', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Student_housing_preferences.py')

if st.button('Connect with Alumni or Students', 
            type='primary', 
            use_container_width=True):
  st.switch_page('pages/31_connect_to_student.py')

if st.button('Edit Parent Housing Relationship',
            type='primary', 
            use_container_width=True):
  st.switch_page('pages/40_parent.py')
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

if st.button('Update Housing Preferences', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Student_housing Preferences.py')
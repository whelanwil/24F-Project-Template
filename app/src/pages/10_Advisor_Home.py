import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Co-op Advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Search Alumni Housing', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/31_Alumn_Housing.py')

if st.button('Track Student Housing Status', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/01_Track_Student_Housing.py')

if st.button('View Alumni-Student Mapping', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/33_Connect_with_Alumni.py')
  

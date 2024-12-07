import logging
import streamlit as st
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

st.title(f"Welcome Co-op Advisor, {st.session_state['first_name']}!")
st.write('')
st.write('### What would you like to do today?')

# Button to search alumni housing (shared with students)
if st.button('Search Alumni Housing', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/11_Alumn_Housing.py')  # Shared page

# Button to connect with alumni or students (shared with students)
if st.button('Connect Students with Alumni', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/12_connect_to_student.py')  # Shared page

# Button to track student housing status (advisor-specific)
if st.button('Track Student Housing Status', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/14_View_Student_Prefrences.py')  # Advisor-specific page


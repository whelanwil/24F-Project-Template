import logging
import streamlit as st
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

st.title(f"Welcome System Administrator, {st.session_state['first_name']}!")
st.write('')
st.write('### What would you like to do today?')

# all pages only for system admin

# Button to get, create, and modify status updates
if st.button('Check or Modify System Updates', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/')  

# Button to add and update alumni and student users
if st.button('Add or Modify Users', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/')  

# Button to remove cities from system database
if st.button('Remove City from Database', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/')  

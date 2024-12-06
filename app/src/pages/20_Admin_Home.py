import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

st.title(f"Welcome System Administrator, {st.session_state['first_name']}!")
st.write('')
st.write('### What would you like to do today?')

# all pages only for system admin

# Button to get, create, and modify status updates
if st.button('Check or Modify System Updates', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/42_status_updates.py')  

# Button to add and update alumni and student users
if st.button('Add or Modify Users', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/21_modify_users.py')  


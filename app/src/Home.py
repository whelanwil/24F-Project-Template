##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import requests
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Husky Den')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

# Make a single API call for student data
try:
    student_response = requests.get(f"http://web-api:4000/auth/student/1")
    if student_response.status_code == 200:
        student_data = student_response.json()
        student_firstname = student_data["data"][0]["firstName"]
        student_lastname = student_data["data"][0]["lastName"]
        student_city = student_data["data"][0]["city"]
        student_id = 1  # Store the ID we used in the API call
    else:
        st.error(f"Error: {student_response.status_code}")
        st.code(student_response.text)
except Exception as e:
    st.error(f"Failed to fetch student data: {str(e)}")

# Make API call for advisor data
try:
    advisor_response = requests.get(f"http://web-api:4000/auth/advisor/1")
    if advisor_response.status_code == 200:
        advisor_data = advisor_response.json()
        advisor_firstname = advisor_data["data"][0]["firstName"]
        advisor_lastname = advisor_data["data"][0]["lastName"]
        advisor_id = 1  # Store the ID we used in the API call
    else:
        st.error(f"Error: {advisor_response.status_code}")
        st.code(advisor_response.text)
except Exception as e:
    st.error(f"Failed to fetch advisor data: {str(e)}")

# Make API call for admin data
try:
    admin_response = requests.get(f"http://web-api:4000/auth/admin/1")
    if admin_response.status_code == 200:
        admin_data = admin_response.json()
        admin_firstname = admin_data["data"][0]["firstName"]
        admin_lastname = admin_data["data"][0]["lastName"]
        admin_id = 1  # Store the ID we used in the API call
    else:
        st.error(f"Error: {admin_response.status_code}")
        st.code(admin_response.text)
except Exception as e:
    st.error(f"Failed to fetch admin data: {str(e)}")

# Make API call for alumni data
try:
    alumni_response = requests.get(f"http://web-api:4000/auth/alumni/1")
    if alumni_response.status_code == 200:
        alumni_data = alumni_response.json()
        alumni_firstname = alumni_data["data"][0]["firstName"]
        alumni_lastname = alumni_data["data"][0]["lastName"]
        alumni_id = 1  # Store the ID we used in the API call
    else:
        st.error(f"Error: {alumni_response.status_code}")
        st.code(alumni_response.text)
except Exception as e:
    st.error(f"Failed to fetch alumni data: {str(e)}")


if st.button(f"Act as {student_firstname} {student_lastname}, a Student on Coop", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = student_firstname
    st.session_state['city'] = student_city
    st.session_state['user_id'] = student_id  # Store the user ID
    logger.info("Logging in as a Student on Coop")
    st.switch_page('pages/00_Student_Home.py')

if st.button(f'Act as {advisor_firstname} {advisor_lastname}, an Coop Advisor', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'advisor'
    st.session_state['first_name'] = advisor_firstname
    st.session_state['user_id'] = advisor_id  # Store the user ID
    st.switch_page('pages/10_Advisor_Home.py')

if st.button(f'Act as {alumni_firstname} {alumni_lastname}, an Alumni', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'alumni'
    st.session_state['first_name'] = alumni_firstname
    st.session_state['user_id'] = alumni_id  # Store the user ID
    st.switch_page('pages/30_Alumni_Home.py')

if st.button(f'Act as {admin_firstname} {admin_lastname}, a System Administrator', 
            type = 'primary', 
            use_container_width=True): 
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = admin_firstname
    st.session_state['user_id'] = admin_id  # Store the user ID
    st.switch_page('pages/20_Admin_Home.py')


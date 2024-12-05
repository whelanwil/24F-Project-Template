import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

if 'user_id' not in st.session_state:
    st.error('You must be logged in as a student to update your information.')
else:
    student_id = st.session_state['user_id']
    st.title("Update Profile Information")

    api_url = f"http://web-api:4000/student/{student_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        student_info = response.json()

        major = student_info.get('major', '')
        company = student_info.get('company', '')
        city = student_info.get('city', '')

        st.subheader('Your Current Information:')
        st.write(f'**Major**: {major}')
        st.write(f'**Company**: {company}')
        st.write(f'**City**: {city}')

        st.subheader('Fill out the following to update your information:')
        with st.form('update_student_info_form'):
            new_major = st.text_input('Major', value=major)
            new_company = st.text_input('Company', value=company)
            new_city = st.text_input('City', value=city)

            submitted = st.form_submit_button('Update Information')

            if submitted:
                data = {
                    'major': new_major,
                    'company': new_company,
                    'city': new_city,
                }
                
                update_response = requests.put(f'http://web-api:4000/student/{student_id}', json=data)
                if update_response.status_code == 200:
                    st.success('Your information has been updated successfully!')
                else:
                    st.error(f'Failed to update information: {update_response.text}')

    else: 
        st.error(f'Failed to fetch student information (Status Code: {response.status_code})')
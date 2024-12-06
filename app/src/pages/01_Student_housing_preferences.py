import logging
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

if 'user_id' not in st.session_state:
    st.error('You must be logged in as a student to update your information.')
else:
    student_id = st.session_state['user_id']
    st.title("Update Profile Information")

    # Fetch student data from the GET route
    api_url = f"http://web-api:4000/student/student/{student_id}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            st.write(data)
            # Convert the list response to a DataFrame
            df = pd.DataFrame(data)
            
            # Get the first row as a dictionary
            student_info = df.iloc[0].to_dict() if not df.empty else {}
            
            major = student_info.get('major', 'N/A')
            company = student_info.get('company', 'N/A')
            city = student_info.get('city', 'N/A')

            # Display the current student information
            st.subheader('Your Current Information:')
            st.write(f'**Major**: {major}')
            st.write(f'**Company**: {company}')
            st.write(f'**City**: {city}')

            # Form for updating information
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

                update_response = requests.put(f'http://web-api:4000/student/student/{student_id}', json=data)

                if update_response.status_code == 200:
                        st.success('Your information has been updated successfully!')
                        st.rerun()
                else:
                        st.error(f'Failed to update information: {update_response.text}')
        except requests.exceptions.JSONDecodeError:
            st.error(f"Error parsing response from server. Response text: {response.text}")
    else:
        st.error(f'Failed to fetch student information (Status Code: {response.status_code})')
        if response.text:
            st.write("Error details:", response.text)

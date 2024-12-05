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
    student_id = st.session_state['user_id']  # Get the logged-in student ID
    st.title("Update Profile Information")

    # Fetch student data from the GET route
    api_url = f"http://web-api:4000/student/{student_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the response JSON
        student_info = response.json()

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
                # Prepare updated data for PUT request
                data = {
                    'major': new_major,
                    'company': new_company,
                    'city': new_city,
                }

                # Send a PUT request to update student information
                update_response = requests.put(f'http://web-api:4000/student/{student_id}', json=data)

                if update_response.status_code == 200:
                    st.success('Your information has been updated successfully!')
                    
                    # Refresh the page to display updated information
                    st.write("**Updated Information:**")
                    st.write(f"**Major**: {new_major}")
                    st.write(f"**Company**: {new_company}")
                    st.write(f"**City**: {new_city}")
                else:
                    st.error(f'Failed to update information: {update_response.text}')
    else:
        st.error(f'Failed to fetch student information (Status Code: {response.status_code})')

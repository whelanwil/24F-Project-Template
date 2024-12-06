import logging
import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from modules.nav import SideBarLinks

# Add sidebar links
SideBarLinks()

# Set up logging
logger = logging.getLogger(__name__)

# Initialize response
response = None

# Check the role of the user
if "role" not in st.session_state:
    st.error("You do not have permission to access this page.")

else:
    role = st.session_state["role"]

    # If the user is a system administrator
    if role in ["administrator"]:
        st.title("Modify Users")
        
        # Create tabs for different actions
        tab1, tab2, tab3 = st.tabs(["Add Alumni", "Update Alumni Information", "Add Student"])

        with tab1:
            st.subheader("Add a New Alumni to the Database")

            with st.form("new_alum_form"):
                firstName = st.text_area("First Name")
                lastName = st.text_area("Last Name")
                email = st.text_area("Email")
                company = st.text_area("Current Company")
                city = st.text_input("City")
                major = st.text_input("Major")
                
                if st.form_submit_button("Add Alumni"):
                    
                    data = {
                        "firstName": firstName,
                        "lastName": lastName,
                        "email": email,
                        "company": company,
                        "city": city,
                        "major": major
                    }
                    
                    response = requests.post("http://web-api:4000/systemAdministrator/update", json=data)
                    if response.status_code == 200:
                        st.success("New alumni added successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to add alumni. Please try again.")
        
        with tab2:
            st.subheader("Update Existing Alumni Information")

            alumID = st.text_input("Enter Alumni ID:")
            if alumID:
                api_url = f"http://web-api:4000/systemAdministrator/alumni/{alumID}"
                response = requests.put(api_url)

            if response.status_code == 200:
                data = response.json()
                
                # Convert the list response to a DataFrame
                df = pd.DataFrame(data)
                
                # Get the first row as a dictionary
                alumni_info = df.iloc[0].to_dict() if not df.empty else {}

                firstName = alumni_info.get('firstName', '')
                lastName = alumni_info.get('lastName', '')
                email = alumni_info.get('email', '')
                company = alumni_info.get('company', '')
                city = alumni_info.get('city', '')
                major = alumni_info.get('major', '')

                st.subheader('Current Information:')
                st.write(f'**First Name**: {firstName}')
                st.write(f'**Last Name**: {lastName}')
                st.write(f'**Email**: {email}')
                st.write(f'**Company**: {company}')
                st.write(f'**City**: {city}')
                st.write(f'**Major**: {major}')

                st.subheader('Fill out the following to update alumni information:')
                with st.form('update_alum_info_form'):
                    new_firstName = st.text_input('First Name:', value=firstName)
                    new_lastName = st.text_input('Last Name:', value=lastName)
                    new_email = st.text_input('Email:', value=email)
                    new_company = st.text_input('Company:', value=company)
                    new_city = st.text_input('City', value=city)
                    new_major = st.text_input('Major', value=major)

                    submitted = st.form_submit_button('Update Information')

                    if submitted:
                        data = {
                            'firstName': new_firstName,
                            'lastName': new_lastName,
                            'email': new_email,
                            'company': new_company,
                            'city': new_city,
                            'major': new_major,
                        }
                        
                        update_response = requests.put(api_url, json=data)
                        if update_response.status_code == 200:
                            st.success('Your information has been updated successfully!')
                            st.rerun()

                        else:
                            st.error(f'Failed to update information: {update_response.text}')

            else: 
                st.error(f'Failed to fetch alumni information (Status Code: {response.status_code})')

        with tab3:
            st.subheader("Add a New Student to the Database")

            with st.form("new_student_form"):
                firstName = st.text_area("First Name")
                lastName = st.text_area("Last Name")
                email = st.text_area("Email")
                major = st.text_area("Major")
                company = st.text_area("Current Co-Op Company")
                city = st.text_input("City")
                
                if st.form_submit_button("Add Student"):
                    
                    data = {
                        "firstName": firstName,
                        "lastName": lastName,
                        "email": email,
                        "major": major,
                        "company": company,
                        "city": city
                    }
                    
                    response = requests.post("http://web-api:4000/systemAdministrator/alumni", json=data)
                    if response.status_code == 200:
                        st.success("New student added successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to add student. Please try again.")

    # If the user has an unrecognized role
    else:
        st.error("Unrecognized role.")

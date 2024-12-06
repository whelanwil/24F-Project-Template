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

# Check the role of the user
if "role" not in st.session_state:
    st.error("You do not have permission to access this page.")

else:
    role = st.session_state["role"]

    # If the user is a system administrator
    if role in ["administrator"]:
        st.title("Modify Users")
        
        # Create tabs for different actions
        tab1, tab2, tab3 = st.tabs(["Alumni", "Students", "Advisors"])

        with tab1:
            st.subheader("Alumni Management")
            
            # Create subtabs for alumni actions
            alumni_tab1, alumni_tab2, alumni_tab3 = st.tabs(["View All Alumni", "Add Alumni", "Update Alumni"])
            
            with alumni_tab1:
                st.subheader("All Alumni in System")
                try:
                    response = requests.get("http://web-api:4000/admin/systemAdministrator/alumni")
                    if response.status_code == 200:
                        alumni_data = response.json()
                        if alumni_data:
                            df = pd.DataFrame(alumni_data)
                            st.dataframe(df)
                        else:
                            st.info("No alumni found in the system.")
                    else:
                        st.error(f"Failed to fetch alumni data. Status code: {response.status_code}")
                except Exception as e:
                    st.error(f"Error fetching alumni data: {str(e)}")
            
            with alumni_tab2:
                st.subheader("Add a New Alumni")
                with st.form("new_alum_form"):
                    firstName = st.text_input("First Name")
                    lastName = st.text_input("Last Name")
                    email = st.text_input("Email")
                    company = st.text_input("Company")
                    city = st.text_input("City")
                    
                    if st.form_submit_button("Add Alumni"):
                        data = {
                            "firstName": firstName,
                            "lastName": lastName,
                            "email": email,
                            "company": company,
                            "city": city
                        }
                        
                        response = requests.post("http://web-api:4000/admin/systemAdministrator/alumni", json=data)
                        if response.status_code == 200:
                            st.success("New alumni added successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to add alumni. Error: {response.text}")
            
            with alumni_tab3:
                st.subheader("Update Existing Alumni Information")
                alumID = st.text_input("Enter Alumni ID:")
                if alumID:
                    api_url = f"http://web-api:4000/admin/systemAdministrator/alumni/{alumID}"
                    response = requests.get(api_url)

                    if response.status_code == 200:
                        data = response.json()
                        alumni_info = data.get('data', [{}])[0]

                        with st.form('update_alum_info_form'):
                            new_firstName = st.text_input('First Name:', value=alumni_info.get('firstName', ''))
                            new_lastName = st.text_input('Last Name:', value=alumni_info.get('lastName', ''))
                            new_email = st.text_input('Email:', value=alumni_info.get('email', ''))
                            new_company = st.text_input('Company:', value=alumni_info.get('company', ''))
                            new_city = st.text_input('City:', value=alumni_info.get('city', ''))

                            if st.form_submit_button('Update Information'):
                                update_data = {
                                    'firstName': new_firstName,
                                    'lastName': new_lastName,
                                    'email': new_email,
                                    'company': new_company,
                                    'city': new_city
                                }
                                
                                update_response = requests.put(api_url, json=update_data)
                                if update_response.status_code == 200:
                                    st.success('Alumni information updated successfully!')
                                    st.rerun()
                                else:
                                    st.error(f'Failed to update information: {update_response.text}')
                    else:
                        st.error(f'Failed to fetch alumni information (Status Code: {response.status_code})')

        with tab2:
            st.subheader("Student Management")
            
            # Create subtabs for student actions
            student_tab1, student_tab2, student_tab3 = st.tabs(["View All Students", "Add Student", "Update Student"])
            
            with student_tab1:
                st.subheader("All Students in System")
                try:
                    response = requests.get("http://web-api:4000/admin/systemAdministrator/student")
                    if response.status_code == 200:
                        student_data = response.json()
                        if student_data:
                            df = pd.DataFrame(student_data)
                            st.dataframe(df)
                        else:
                            st.info("No students found in the system.")
                    else:
                        st.error(f"Failed to fetch student data. Status code: {response.status_code}")
                except Exception as e:
                    st.error(f"Error fetching student data: {str(e)}")
            
            with student_tab2:
                st.subheader("Add a New Student")
                with st.form("new_student_form"):
                    firstName = st.text_input("First Name", key="student_first")
                    lastName = st.text_input("Last Name", key="student_last")
                    email = st.text_input("Email", key="student_email")
                    company = st.text_input("Current Co-Op Company")
                    city = st.text_input("City", key="student_city")
                    major = st.text_input("Major")
                    admin_id = st.text_input('Admin ID')
                    advisor_id = st.text_input('Advisor ID')
                    
                    if st.form_submit_button("Add Student"):
                        data = {
                            "firstName": firstName,
                            "lastName": lastName,
                            "email": email,
                            "major": major,
                            "company": company,
                            "city": city,
                            "admin_id": admin_id,
                            "advisor_id": advisor_id
                        }
                        
                        response = requests.post("http://web-api:4000/admin/systemAdministrator/student", json=data)
                        if response.status_code == 200:
                            st.success("New student added successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to add student. Error: {response.text}")
            
            with student_tab3:
                st.subheader("Update Existing Student Information")
                studentID = st.text_input("Enter Student ID:")
                if studentID:
                    api_url = f"http://web-api:4000/admin/systemAdministrator/student/{studentID}"
                    response = requests.get(api_url)

                    if response.status_code == 200:
                        data = response.json()
                        student_info = data.get('data', [{}])[0]

                        with st.form('update_student_info_form'):
                            new_firstName = st.text_input('First Name:', value=student_info.get('firstName', ''))
                            new_lastName = st.text_input('Last Name:', value=student_info.get('lastName', ''))
                            new_email = st.text_input('Email:', value=student_info.get('email', ''))
                            new_company = st.text_input('Company:', value=student_info.get('company', ''))
                            new_city = st.text_input('City:', value=student_info.get('city', ''))
                            new_major = st.text_input('Major:', value=student_info.get('major', ''))
                            new_advisor_id = st.text_input('Advisor ID:', value=student_info.get('advisorID', ''))

                            if st.form_submit_button('Update Information'):
                                update_data = {
                                    'firstName': new_firstName,
                                    'lastName': new_lastName,
                                    'email': new_email,
                                    'company': new_company,
                                    'city': new_city,
                                    'major': new_major,
                                    'advisor_id': new_advisor_id
                                }
                                
                                update_response = requests.put(api_url, json=update_data)
                                if update_response.status_code == 200:
                                    st.success('Student information updated successfully!')
                                    st.rerun()
                                else:
                                    st.error(f'Failed to update information: {update_response.text}')
                    else:
                        st.error(f'Failed to fetch student information (Status Code: {response.status_code})')

        with tab3:
            st.subheader("Advisor Management")
            
            # Create subtabs for advisor actions
            advisor_tab1, advisor_tab2, advisor_tab3 = st.tabs(["View All Advisors", "Add Advisor", "Update Advisor"])
            
            with advisor_tab1:
                st.subheader("All Advisors in System")
                try:
                    response = requests.get("http://web-api:4000/admin/systemAdministrator/advisor")
                    if response.status_code == 200:
                        advisor_data = response.json()
                        if advisor_data:
                            df = pd.DataFrame(advisor_data)
                            st.dataframe(df[['advisorID', 'firstName', 'lastName', 'email', 'department']])
                        else:
                            st.info("No advisors found in the system.")
                    else:
                        st.error(f"Failed to fetch advisor data. Status code: {response.status_code}")
                except Exception as e:
                    st.error(f"Error fetching advisor data: {str(e)}")
            
            with advisor_tab2:
                st.subheader("Add a New Advisor")
                with st.form("new_advisor_form"):
                    firstName = st.text_input("First Name", key="advisor_first")
                    lastName = st.text_input("Last Name", key="advisor_last")
                    email = st.text_input("Email", key="advisor_email")
                    department = st.text_input("Department")
                    
                    if st.form_submit_button("Add Advisor"):
                        data = {
                            "firstName": firstName,
                            "lastName": lastName,
                            "email": email,
                            "department": department
                        }
                        
                        response = requests.post("http://web-api:4000/admin/systemAdministrator/advisor", json=data)
                        if response.status_code == 200:
                            st.success("New advisor added successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to add advisor. Error: {response.text}")
            
            with advisor_tab3:
                st.subheader("Update Existing Advisor Information")
                advisorID = st.text_input("Enter Advisor ID:")
                if advisorID:
                    api_url = f"http://web-api:4000/admin/systemAdministrator/advisor/{advisorID}"
                    response = requests.get(api_url)

                    if response.status_code == 200:
                        data = response.json()
                        advisor_info = data.get('data', [{}])[0]

                        with st.form('update_advisor_info_form'):
                            new_firstName = st.text_input('First Name:', value=advisor_info.get('firstName', ''))
                            new_lastName = st.text_input('Last Name:', value=advisor_info.get('lastName', ''))
                            new_email = st.text_input('Email:', value=advisor_info.get('email', ''))
                            new_department = st.text_input('Department:', value=advisor_info.get('department', ''))

                            if st.form_submit_button('Update Information'):
                                update_data = {
                                    'firstName': new_firstName,
                                    'lastName': new_lastName,
                                    'email': new_email,
                                    'department': new_department
                                }
                                
                                update_response = requests.put(api_url, json=update_data)
                                if update_response.status_code == 200:
                                    st.success('Advisor information updated successfully!')
                                    st.rerun()
                                else:
                                    st.error(f'Failed to update information: {update_response.text}')
                    else:
                        st.error(f'Failed to fetch advisor information (Status Code: {response.status_code})')

    # If the user has an unrecognized role
    else:
        st.error("You do not have permission to access this page.")

import logging
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(page_title="Co-op Advisor: Student Information", layout="wide")

# Set up logging
logger = logging.getLogger(__name__)

# API Base URL
BASE_API_URL = "http://web-api:4000"

# Title
st.title("Co-op Advisor Dashboard: View Student Housing Preferences")

# Input for Student nuID
student_id = st.text_input("Enter Student nuID:", "")

# Fetch Student Information
if st.button("Get Student Information"):
    if student_id.isdigit():
        try:
            # Make the GET request
            response = requests.get(f"{BASE_API_URL}/student/{student_id}")

            if response.status_code == 200:
                # Parse the student data
                student_data = response.json().get("student", {})
                
                # Display student information
                st.subheader("Student Information")
                st.write(f"**nuID**: {student_data.get('nuID', 'N/A')}")
                st.write(f"**First Name**: {student_data.get('firstName', 'N/A')}")
                st.write(f"**Last Name**: {student_data.get('lastName', 'N/A')}")
                st.write(f"**Major**: {student_data.get('major', 'N/A')}")
                st.write(f"**Company**: {student_data.get('company', 'N/A')}")
                st.write(f"**City**: {student_data.get('city', 'N/A')}")

            elif response.status_code == 404:
                st.warning("Student not found.")
            else:
                st.error(f"Error fetching student information: {response.status_code} - {response.text}")

        except requests.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid numeric Student nuID.")
import logging
import streamlit as st
import requests
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

    # Only advisors can access this page
    if role == "advisor":
        st.title("Assign Alumni to Student")

        # Input fields
        student_id = st.text_input("Enter the Student ID:")
        alumni_id = st.text_input("Enter the Alumni ID:")

        if st.button("Assign Alumni"):
            if student_id and alumni_id:
                # API endpoint
                api_url = f"http://web-api:4000/coOpAdvisor/student/{student_id}/alumni"

                # Payload
                payload = {"alumniID": alumni_id}

                # Make the PUT request
                response = requests.put(api_url, json=payload)

                # Handle response
                if response.status_code == 200:
                    st.success(response.json().get("message", "Alumni assigned successfully"))
                elif response.status_code == 400:
                    st.warning(response.json().get("error", "Invalid request"))
                elif response.status_code == 404:
                    st.error(response.json().get("error", "Student not found"))
                else:
                    st.error(f"Failed to assign alumni. Error: {response.status_code}")
            else:
                st.warning("Both Student ID and Alumni ID are required.")
    else:
        st.error("You do not have permission to access this page.")
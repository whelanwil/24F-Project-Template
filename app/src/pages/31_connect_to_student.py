import logging
import streamlit as st
import requests

# Set up logging
logger = logging.getLogger(__name__)

# Check the role of the user
if "role" not in st.session_state:
    st.error("You do not have permission to access this page.")
else:
    role = st.session_state["role"]

    if role == "advisor":
        st.title("Assign Alumni to a Student")

        # Inputs for assigning alumni to a student
        student_id = st.number_input("Enter the Student ID", min_value=1, step=1)
        alumni_id = st.number_input("Enter the Alumni ID", min_value=1, step=1)

        if st.button("Assign Alumni", use_container_width=True):
            if student_id and alumni_id:
                # Prepare the payload
                payload = {"alumniID": alumni_id}

                # API URL
                api_url = f"http://web-api:4000/coOpAdvisor/student/{student_id}/alumni"

                # Make the PUT request
                response = requests.put(api_url, json=payload)

                if response.status_code == 200:
                    st.success(response.json().get("message", "Alumni assigned successfully"))
                elif response.status_code == 400:
                    st.warning(response.json().get("error", "Invalid request"))
                elif response.status_code == 404:
                    st.error(response.json().get("error", "Student not found"))
                else:
                    st.error("Failed to assign alumni. Please try again later.")
            else:
                st.warning("Please enter both Student ID and Alumni ID.")
    else:
        st.error("Only advisors can access this page.")
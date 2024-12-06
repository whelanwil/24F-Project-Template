import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Add sidebar navigation links
SideBarLinks()

# Base API URL
BASE_API_URL = ""

# Page Title
st.title("Manage Alum-Student Connections")

# Tabs for different actions
tab1, tab2, tab3 = st.tabs(["View Connections", "Add Connection", "Remove Connection"])

# Tab 1: View Connections
with tab1:
    st.subheader("View All Alum-Student Connections")
    try:
        response = requests.get(f'http://web-api:4000/studentAlum/alumstudent)
        st.write("Status Code:", response.status_code)
        st.write("Response Content:", response.text)

        if response.status_code == 200:
            connections = response.json().get("data", [])
            if connections:
                st.table(pd.DataFrame(connections))
            else:
                st.info("No alum-student connections found.")
        else:
            # Extract the actual error message from the API response
            error_message = response.json().get("error", "Unknown error")
            st.error(f"Failed to retrieve connections: {error_message}")
    except requests.RequestException as e:
        st.error(f"An error occurred while retrieving connections: {str(e)}")

# Tab 2: Add Connection
with tab2:
    st.subheader("Add a New Connection")

    # Input fields for adding a connection
    student_id = st.text_input("Enter the Student ID:")
    alumni_id = st.text_input("Enter the Alumni ID:")

    if st.button("Add Connection"):
        if student_id and alumni_id:
            payload = {"nuID": student_id, "alumID": alumni_id}
            try:
                response = requests.post(BASE_API_URL, json=payload, timeout=10)
                if response.status_code == 201:
                    st.success(response.json().get("message", "Connection added successfully!"))
                elif response.status_code == 400:
                    st.warning(response.json().get("error", "Invalid input. Please check the IDs and try again."))
                else:
                    error_message = response.json().get("error", "Unknown error")
                    st.error(f"Failed to add connection: {error_message}")
            except requests.RequestException as e:
                st.error(f"An error occurred while adding the connection: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")

# Tab 3: Remove Connection
with tab3:
    st.subheader("Remove an Existing Connection")

    # Input fields for removing a connection
    student_id = st.text_input("Enter the Student ID to remove:", key="remove_student")
    alumni_id = st.text_input("Enter the Alumni ID to remove:", key="remove_alumni")

    if st.button("Remove Connection"):
        if student_id and alumni_id:
            delete_url = f"{BASE_API_URL}/{student_id}/{alumni_id}"
            try:
                response = requests.delete(delete_url, timeout=10)
                if response.status_code == 200:
                    st.success(response.json().get("message", "Connection removed successfully!"))
                elif response.status_code == 404:
                    st.warning(response.json().get("error", "Connection not found."))
                else:
                    error_message = response.json().get("error", "Unknown error")
                    st.error(f"Failed to remove connection: {error_message}")
            except requests.RequestException as e:
                st.error(f"An error occurred while removing the connection: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

SideBarLinks()

# Base API URL
BASE_API_URL = "http://web-api:4000/studentAlum/alumstudent"

# Page Title
st.title("Manage Alum-Student Connections")

# Tabs for different actions
tab1, tab2, tab3 = st.tabs(["View Connections", "Add Connection", "Remove Connection"])

# Tab 1: View Connections
with tab1:
    st.subheader("View All Alum-Student Connections")
<<<<<<< HEAD
    st.write("here 1")
    response = requests.get(BASE_API_URL)
    st.write("here 2")
    # Display the status code and response for debugging
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
=======

    try:
        response = requests.get(BASE_API_URL)
        st.write("Status Code:", response.status_code)
        
        if response.status_code == 200:
            # Parse JSON response
            try:
                connections = response.json().get("data", [])
                if connections:
                    st.table(pd.DataFrame(connections))
                else:
                    st.info("No alum-student connections found.")
            except ValueError:
                st.error("Failed to parse JSON response from the server.")
        elif response.status_code == 404:
            st.warning("No connections found. The API endpoint might not exist.")
        else:
            st.error(f"Unexpected error: {response.text}")
    except requests.RequestException as e:
        st.error(f"An error occurred while connecting to the API: {str(e)}")
>>>>>>> aa1323f4c9ce5a70315d8de8e3117fabb33af5f1

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
                response = requests.post(BASE_API_URL, json=payload)
                if response.status_code == 201:
                    st.success(response.json().get("message", "Connection added successfully!"))
                elif response.status_code == 400:
                    st.warning(response.json().get("error", "Invalid input. Please check the IDs and try again."))
                else:
                    st.error("Failed to add connection. Please try again.")
            except requests.RequestException as e:
                st.error(f"An error occurred while adding the connection: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")

# Tab 3: Remove Connection
with tab3:
    st.subheader("Remove an Existing Connection")

    student_id = st.text_input("Enter the Student ID to remove:", key="remove_student")
    alumni_id = st.text_input("Enter the Alumni ID to remove:", key="remove_alumni")

    if st.button("Remove Connection"):
        if student_id and alumni_id:
            delete_url = f"{BASE_API_URL}/{student_id}/{alumni_id}"
            try:
                response = requests.delete(delete_url)
                if response.status_code == 200:
                    st.success(response.json().get("message", "Connection removed successfully!"))
                elif response.status_code == 404:
                    st.warning(response.json().get("error", "Connection not found."))
                else:
                    st.error("Failed to remove connection. Please try again.")
            except requests.RequestException as e:
                st.error(f"An error occurred while removing the connection: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")

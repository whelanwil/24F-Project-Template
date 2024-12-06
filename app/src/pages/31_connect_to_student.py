import streamlit as st
import time
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
# Tab 1: View Connections
with tab1:
    st.subheader("View All Alum-Student Connections")
    
    try:
        response = requests.get(BASE_API_URL)
        
        if response.status_code == 200:
            # Parse the response and retrieve the data
            connections = response.json().get("data", [])
            if connections:
                # Display the data as a table
                st.table(pd.DataFrame(connections))
            else:
                # Inform the user if no connections are found
                st.info("No alum-student connections found.")
        else:
            # Handle API errors and display the error message
            error_message = response.json().get("error", "An unknown error occurred.")
            st.error(f"Failed to retrieve connections: {error_message}")
    except requests.RequestException as e:
        # Handle request exceptions and display the error
        st.error(f"Error retrieving connections: {str(e)}")

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
                # Remove debug prints
                response = requests.post(BASE_API_URL, json=payload)
                
                if response.status_code == 201:
                    st.success(response.json().get("message", "Connection added successfully!"))
                    time.sleep(1)
                    st.rerun()
                elif response.status_code == 400:
                    st.warning(response.json().get("error", "Invalid input. Please check the IDs and try again."))
                else:
                    st.error(f"Failed to add connection. Server response: {response.json()}")
            except requests.RequestException as e:
                st.error(f"An error occurred while adding the connection: {str(e)}")
            except ValueError as e:
                st.error(f"Error parsing response: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")

with tab3:
    st.subheader("Remove an Existing Connection")

    student_id = st.text_input("Enter the Student ID to remove:", key="remove_student")
    alumni_id = st.text_input("Enter the Alumni ID to remove:", key="remove_alumni")

    if st.button("Remove Connection"):
        if student_id and alumni_id:
            # Construct the delete URL using the same base URL
            delete_url = f"{BASE_API_URL}/{student_id}/{alumni_id}"
            st.write("Attempting to delete at URL:", delete_url)  # Debug line
            try:
                response = requests.delete(delete_url)
                try:
                    response_data = response.json()
                    if response.status_code == 200:
                        st.success(response_data.get("message", "Connection removed successfully!"))
                        time.sleep(1)
                        st.rerun()
                    elif response.status_code == 404:
                        st.warning(response_data.get("error", "Connection not found."))
                    else:
                        st.error(f"Failed to remove connection: {response_data.get('error', 'Unknown error')}")
                except ValueError:
                    st.error(f"Invalid response from server. Status code: {response.status_code}")
            except requests.RequestException as e:
                st.error(f"Network error while removing the connection: {str(e)}")
        else:
            st.warning("Both Student ID and Alumni ID are required.")
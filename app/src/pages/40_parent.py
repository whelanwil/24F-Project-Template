import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Page setup must come first
st.set_page_config(page_title="Edit Parent Housing Relationship", layout="wide")

# Add sidebar navigation
SideBarLinks()

st.title("Edit Parent Housing Relationship")

# Logged-in user's ID
student_id = st.session_state.get('user_id')  # Assume user_id is set in session_state
if not student_id:
    st.error("You must be logged in to manage parent relationships.")
    st.stop()

# Tabs for managing parent relationships
tab1, tab2, tab3 = st.tabs(["View Parents", "Add Parent", "Remove Parent"])

# Tab 1: View Parents
with tab1:
    st.subheader("Your Current Parents")
    try:
        # Fetch parents from API
        response = requests.get(f"http://web-api:4000/student/student/parents/{student_id}")
        if response.status_code == 200:
            parents = response.json()
            if parents:
                df = pd.DataFrame(parents)
                df = df[['parentID', 'firstName', 'lastName', 'relationshipToStudent', 'email', 'phone']]
                st.table(df)
            else:
                st.info("No parents found for your account.")
        else:
            st.error("Failed to fetch parent information. Please try again.")
    except requests.RequestException as e:
        st.error(f"An error occurred: {str(e)}")

# Tab 2: Add Parent
with tab2:
    st.subheader("Add a New Parent")
    with st.form("add_parent_form"):
        first_name = st.text_input("First Name", max_chars=50)
        last_name = st.text_input("Last Name", max_chars=50)
        email = st.text_input("Email", max_chars=100)
        phone = st.text_input("Phone (optional)", max_chars=15)
        relationship = st.selectbox(
            "Relationship to Student",
            options=[
                "Mother",
                "Father",
                "Guardian",
                "Stepmother",
                "Stepfather",
                "Grandparent",
                "Foster Parent",
                "Legal Guardian",
                "Adoptive Parent"
            ]
        )
        submitted = st.form_submit_button("Add Parent")

        if submitted:
            if not (first_name and last_name and email and relationship):
                st.warning("First Name, Last Name, Email, and Relationship are required.")
            else:
                payload = {
                    "studentID": student_id,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "phone": phone or None,
                    "relationshipToStudent": relationship
                }
                try:
                    response = requests.post("http://web-api:4000/student/student/parent", json=payload)
                    if response.status_code == 201:
                        st.success("Parent added successfully!")
                        st.rerun()
                    else:
                        st.error(f"Failed to add parent: {response.json().get('error', 'Unknown error')}")
                except requests.RequestException as e:
                    st.error(f"An error occurred: {str(e)}")

# Tab 3: Remove Parent
with tab3:
    st.subheader("Remove Parent Access")
    try:
        # Fetch current parents for selection
        response = requests.get(f"http://web-api:4000/student/student/parents/{student_id}")
        if response.status_code == 200:
            parents = response.json()
            if parents:
                # Create a selection box with parent information
                parent_options = [f"{p['firstName']} {p['lastName']} (ID: {p['parentID']})" for p in parents]
                selected_parent = st.selectbox("Select Parent to Remove", parent_options)
                
                if selected_parent:
                    # Extract parentID from selection
                    parent_id = int(selected_parent.split("ID: ")[1].rstrip(")"))
                    
                    if st.button("Remove Selected Parent", type="secondary"):
                        try:
                            # Send delete request with both parentID and studentID
                            response = requests.delete(
                                f"http://web-api:4000/student/student/parent/{parent_id}",
                                json={"studentID": student_id}
                            )
                            
                            if response.status_code == 200:
                                st.success("Parent access removed successfully!")
                                st.rerun()
                            else:
                                st.error("Failed to remove parent access. Please try again.")
                        except requests.RequestException as e:
                            st.error(f"An error occurred: {str(e)}")
            else:
                st.info("No parents found to remove.")
    except requests.RequestException as e:
        st.error(f"An error occurred while fetching parents: {str(e)}")

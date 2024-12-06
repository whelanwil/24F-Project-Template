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
        print(response.json())
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
                    "studentID": student_id,  # Using the student_id from session state
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
    st.subheader("Remove a Parent")
    with st.form("remove_parent_form"):
        remove_confirmation = st.checkbox("I confirm to remove all parents associated with my account.")
        submitted_remove = st.form_submit_button("Remove Parents")

        if submitted_remove:
            if remove_confirmation:
                try:
                    response = requests.delete('http://web-api:4000/student/student/parent')
                    if response.status_code == 200:
                        st.success("All parents have been removed successfully.")
                    else:
                        st.error(f"Failed to remove parents: {response.text}")
                except requests.RequestException as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please confirm to proceed with removing parents.")

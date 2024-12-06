import streamlit as st
import requests
import pandas as pd

BASE_API_URL = "http://web-api:4000/student/student"  # Base API URL

# Page setup
st.set_page_config(page_title="Edit Parent Housing Relationship", layout="wide")
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
        response = requests.get(f"{BASE_API_URL}/{student_id}/parents")
        if response.status_code == 200:
            parents = response.json().get("parents", [])
            if parents:
                df = pd.DataFrame(parents)
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
        submitted = st.form_submit_button("Add Parent")

        if submitted:
            if not (first_name and last_name and email):
                st.warning("First Name, Last Name, and Email are required.")
            else:
                payload = {
                    "nuID": student_id,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "phone": phone or None,
                }
                try:
                    response = requests.post(f"{BASE_API_URL}/parent", json=payload)
                    if response.status_code == 201:
                        st.success("Parent added successfully!")
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
                    response = requests.delete(BASE_API_URL)
                    if response.status_code == 200:
                        st.success("All parents have been removed successfully.")
                    else:
                        st.error(f"Failed to remove parents: {response.text}")
                except requests.RequestException as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please confirm to proceed with removing parents.")

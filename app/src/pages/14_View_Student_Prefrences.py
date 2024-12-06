import logging
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

def style_housing_status(df):
    return df.style.apply(lambda x: ['background-color: rgba(255, 80, 80, 0.2)' if v == 'Not Housed' 
                                   else 'background-color: rgba(80, 255, 80, 0.2)' if v == 'Housed'
                                   else '' for v in x], 
                         subset=['housingStatus'])  # replace 'housing_status' with your actual column name

# Set page configuration
st.set_page_config(page_title="Co-op Advisor: Student Information", layout="wide")
SideBarLinks()

advisor_id = st.session_state['user_id']

# Set up logging
logger = logging.getLogger(__name__)

# Title
st.title("Co-op Advisor Dashboard: View Student Housing Preferences")

# Create tabs
tab1, tab2 = st.tabs(["My Students", "All Students"])

with tab1:
    st.header("My Students")
    api_url = f"http://web-api:4000/advisor/student/{advisor_id}"    
    response = requests.get(api_url)
    if response.status_code == 200:
        my_students_df = pd.DataFrame(response.json())
    
    if not my_students_df.empty:
        st.dataframe(
            style_housing_status(my_students_df),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No students assigned to you at this time.")
            
with tab2:
    st.header("All Students")
    
    # Search filter
    student_id_filter = st.text_input("Filter by Student ID")
    
    try:
        if student_id_filter:
            # If searching for specific student
            api_url = f"http://web-api:4000/advisor/allstudents/{student_id_filter}"
        else:
            # If no filter, get all students
            api_url = "http://web-api:4000/advisor/allstudents"
            
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert response to DataFrame
            filtered_df = pd.DataFrame(response.json())
            
            if not filtered_df.empty:
                st.dataframe(
                    filtered_df,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No students found matching your criteria.")
        else:
            st.error(f"Error fetching data: {response.status_code}")
            
    except Exception as e:
        st.error(f"Error fetching student data: {str(e)}")


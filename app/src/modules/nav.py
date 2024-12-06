import streamlit as st

# ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


# def AboutPageNav():
#     st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


# ------------------------ Student Role ------------------------
def StudentNav():
    st.sidebar.page_link(
        "pages/00_Student_Home.py", label="Student Dashboard", icon="🎓"
    )
    st.sidebar.page_link(
        "pages/04_Search_Alum_Housing.py", label="Search Alumni Housing", icon="🏘️"
    )
    st.sidebar.page_link(
        "pages/01_Student_housing_preferences.py",
        label="Update Profile Information",
        icon="⚙️",
    )
    st.sidebar.page_link(
        "pages/02_Student_Alumni_Connection.py", label="View Connected Alumni", icon="🤝"
    )
    st.sidebar.page_link(
        "pages/40_parent.py", label="Edit Parent Housing Relationship", icon="👪"
    )


# ------------------------ Advisor Role ------------------------
def AdvisorNav():
    st.sidebar.page_link(
        "pages/10_Advisor_Home.py", label="Advisor Dashboard", icon="📋"
    )
    st.sidebar.page_link(
        "pages/11_Alumn_Housing.py", label="Search Alumni Housing", icon="🏘️"
    )
    st.sidebar.page_link(
        "pages/12_connect_to_student.py", label="Connect with Alumni/Students", icon="🤝"
    )
    st.sidebar.page_link(
        "pages/14_View_Student_Prefrences.py",label="Track Student Housing Status", icon="📊",
    )


# ------------------------ Alumni Role ------------------------
def AlumniNav():
    st.sidebar.page_link(
        "pages/30_Alumni_Home.py", label="Alumni Dashboard", icon="🏡"
    )
  
    st.sidebar.page_link(
        "pages/31_Connect_To_Students.py", label="View Connected Students", icon="🛏️"
    )


# ------------------------ System Admin Role ------------------------
def AdminNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="Admin Dashboard", icon="🖥️")
    


# ------------------------ SideBarLinks Function ------------------------
def SideBarLinks(show_home=False):
    """
    Dynamically manages sidebar links based on the logged-in user's role.
    """

    # Add a logo to the sidebar
    st.sidebar.image("assets/logo.png", width=150)

    # Redirect unauthenticated users to Home
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    # Add the Home page link if specified
    if show_home:
        HomeNav()

    # Display role-specific navigation based on authentication and role
    if st.session_state["authenticated"]:
        role = st.session_state["role"]

        if role == "student":
            StudentNav()
        elif role == "advisor":
            AdvisorNav()
        elif role == "alumni":
            AlumniNav()
        elif role == "administrator":
            AdminNav()

    # Add the About page at the bottom of the sidebar
    # AboutPageNav()

    # Add a logout button for authenticated users
    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")

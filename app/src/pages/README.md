# `pages` Folder

This folder contains all the pages that will be part of the application. Details on required numbers will be provided in the Phase 3 documentation.

These pages are meant to show you an example of some of the features of Streamlit and the way we will limit functionality access by role/persona. It is not meant to represent a complete application.

TODO: Describe the pages folder and include link to documentation. Don't forget about ordering of pages.

# Our pages
Home.py is what houses the home page and contains the links to the four persona subpages. 

## Student page
00_Student_Home.py represents the home page for the Student profile, and contains links to the following pages in 
this order:
- Search Alumni Housing --> 04_Search_Alum_Housing.py
- Update Profile Information --> 01_Student_housing_preferences.py
- Connected Alumni --> 02_Student_Alumni_Connection.py
- Edit Parent Housing Relationship --> 40_parent.py

## Advisor page
10_Advisor_Home.py represents the home page for the Advisor profile, and contains links to the following pages in this order:
- Search Alumni Housing --> 11_Alumn_Housing.py
- Connect Students with Alumni --> 12_connect_to_student.py
- Track Student Housing Status --> 14_View_Student_Prefrences.py

## Alumni page
30_Alumni_Home.py represents the home page for the Alumni profile, and contains links to the following pages in this order:
- Edit Apartment Details --> 30_Edit_Alumni_Housing.py
- Connected Students --> 31_Connect_To_Students.py

## Admin page
20_Admin_Home.py represents the home page for the Admin profile and contains a single page that holds several tabs that house the Admin's functionality. A user can switch from alumni to students to advisors and view, add, update, and delete each persona's information.
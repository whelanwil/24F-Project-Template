# `database-files` Folder

# Husky Den Database

# The tables
The following is a summary of what each of the tables in our database represents:
- SystemAdministrator: A table of system administrators with fields like adminID, firstName, lastName, and email. This is one of our core four personas who represents the person managing the HuskyDen platform and handles the connections and details of app users.

- Alumni: Represents alumni details such as name, major, company, and city. It has a foreign key linking to the SystemAdministrator table. This is one of the core four personas in the app that represents an alumni who is offering housing for students. 

- CoopAdvisor: Represents co-op advisors and their associated SystemAdministrator. This is one of our core four personas who represents a coop advisor that manages the relationship between students and alumni and serves as an advisor for the student on search for coop and housing during that time.

- Student: Represents students, including fields for their major, housing status, and references to an advisor and admin. This is one of our core four personas that represents a student looking for housing during their coop.

- Parent: Stores information about student parents (e.g., name, relationship, contact info). Represents a parent of a student. 

- StudentParent: A mapping table connecting students to their parents (many-to-many relationship). This table represents this relationship between the Student and Parent tables.

- Performance: Tracks system performance metrics like uptime, response time, and error rates.

- Updates: Logs system updates with descriptions and timestamps.

- Apartment: Represents alumni-offered housing options with details like rent, availability, and location.

- Recommendation: Stores alumni recommendations for establishments, categorized by type and price rating.

- AlumAdvisor: Maps alumni to co-op advisors (many-to-many relationship). This table represents this relationship between the Alumni and CoopAdvisor tables.

- AlumStudent: Maps alumni to students (mentorship connections).This table represents this relationship between the Alumni and Student tables.


## To re-bootstrap the interface, do the following:
1. Drop the existing database by using the command:
DROP DATABASE IF EXISTS huskyDenDB;

2. Create the database
CREATE DATABASE huskyDenDB;
USE huskyDenDB;

3. Execute the CREATE TABLE statements which define the tables and relationships in order to recreate the schema

4. Insert the data with the INSERT INTO statements.

5. Verify the data using SQL queries. 
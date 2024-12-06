from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
advisor = Blueprint('advisor', __name__)

# ------------------------------------------------------------
# 4.1 Get all alumni offering housing in a specific city
@advisor.route('/alumni/<city>', methods=['GET'])
def get_alumni_housing(city):
    query = '''
        SELECT A.alumID, A.firstName, A.lastName, Ap.city
        FROM Alumni A
        JOIN Apartment Ap ON A.alumID = Ap.alumID
        WHERE Ap.city = %s
    '''
    
    current_app.logger.info(f'GET /alumni/<city> query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
    

# ------------------------------------------------------------
# Revoke parental access
@advisor.route('/coopAdvisor/communication/parents/<parentID>', methods=['DELETE'])
def revoke_parental_access(parentID):
    current_app.logger.info(f'DELETE /parents/{parentID} route')

    query = '''
        DELETE FROM StudentParent
        WHERE parentID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (parentID,))
    db.get_db().commit()

    if cursor.rowcount > 0:
        response = make_response(f'Parental access revoked for parent ID {parentID}.')
        response.status_code = 200
    else:
        response = make_response(f'No association found for parent ID {parentID}.')
        response.status_code = 404

    return response

# ------------------------------------------------------------
# Add a new student to the database
@advisor.route('/coopAdvisor/student', methods=['POST'])
def add_student_with_city():
    """
    Add a new student to the database by a Co-op Advisor.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    company = data.get('company')
    city = data.get('city')
    admin_id = data.get('adminID')  # Admin ID may still be relevant, but the advisor is the one creating the student.
    advisor_id = data.get('advisorID')  # This should be the Co-op Advisor's ID.

    # Validate required fields
    if not all([first_name, last_name, email, company, city, admin_id, advisor_id]):
        return make_response(
            jsonify({"error": "All fields (firstName, lastName, email, company, city, adminID, advisorID) are required"}),
            400
        )

    # SQL query to insert a new student record
    query = '''
        INSERT INTO Student (firstName, lastName, email, company, city, adminID, advisorID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, company, city, admin_id, advisor_id))
        db.get_db().commit()

        # Success response
        return make_response(
            jsonify({"message": f"Student '{first_name} {last_name}' added successfully by Co-op Advisor ID {advisor_id}"}), 
            201
        )

    except Exception as e:
        # Log and handle errors
        print(f"Error occurred: {e}")
        return make_response(jsonify({"error": "An internal server error occurred"}), 500)
    
# ------------------------------------------------------------
# Edit student information in the database
@advisor.route('/coopAdvisor/student/<int:student_id>/alumni', methods=['PUT'])
def assign_alumni_to_student(student_id):
    """
    Assign an alumni to a student by updating the alumniID field.
    """
    data = request.json

    # Validate input
    if 'alumniID' not in data or not data['alumniID']:
        return make_response(jsonify({"error": "Missing or invalid 'alumniID'"}), 400)

    alumni_id = data['alumniID']

    # Prepare the SQL query
    query = "UPDATE Student SET alumniID = %s WHERE nuID = %s"

    try:
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (alumni_id, student_id))
        db.get_db().commit()

        # Check if a student was updated
        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Student not found or no changes made"}), 404)

        return make_response(jsonify({"message": f"Alumni ID {alumni_id} assigned to Student ID {student_id} successfully"}), 200)

    except Exception as e:
        # Log and handle errors
        print(f"Error occurred: {e}")
        return make_response(jsonify({"error": "An internal server error occurred"}), 500)

@advisor.route('student/<nuID>', methods=['GET'])
def get_student_info(nuID):
    """
    Co-op Advisor route to get a student's information by their nuID.
    """
    current_app.logger.info(f"GET /advisor/student/{nuID} route called")

    # SQL query to fetch the student's details
    query = '''
        SELECT 
            s.nuID, 
            s.firstName, 
            s.lastName, 
            s.major, 
            s.company, 
            s.city
        FROM Student s
        WHERE s.nuID = %s
    '''

    try:
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (nuID,))
        result = cursor.fetchone()

        # If no student is found, return a 404 response
        if not result:
            current_app.logger.warning(f"Student with nuID {nuID} not found")
            return make_response(jsonify({"error": "Student not found"}), 404)

        # Map the result to a dictionary
        student_info = {
            "nuID": result[0],
            "firstName": result[1],
            "lastName": result[2],
            "major": result[3],
            "company": result[4],
            "city": result[5],
        }

        current_app.logger.info(f"Student info retrieved: {student_info}")
        return make_response(jsonify({"student": student_info}), 200)

    except Exception as e:
        current_app.logger.error(f"Error retrieving student info: {str(e)}")
        return make_response(jsonify({"error": "Internal server error"}), 500)
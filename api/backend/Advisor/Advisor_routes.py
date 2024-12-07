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



@advisor.route('/student/<advisorID>', methods=['GET'])
def get_student_info(advisorID):
    """
    Co-op Advisor route to get a student's information by their nuID.
    """
    current_app.logger.info(f"GET /advisor/student/{advisorID} route called")

    # SQL query to fetch the student's details
    query = '''
        SELECT *
        FROM Student s
        WHERE s.advisorID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (advisorID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@advisor.route('/allstudents', methods=['GET'])
def get_all_students():
    """
    Co-op Advisor route to get all students.
    """
    current_app.logger.info(f"GET /advisor/allstudents route called")

    # SQL query to fetch the student's details
    query = '''
        SELECT *
        FROM Student s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#select all studenys by ID
@advisor.route('/allstudents/<nuID>', methods=['GET'])
def get_all_students_by_ID(nuID):
    """
    Co-op Advisor route to get all students by nuID.
    """
    current_app.logger.info(f"GET /advisor/allstudents/{nuID} route called")

    # SQL query to fetch the student's details
    query = '''
        SELECT *
        FROM Student s
        WHERE s.nuID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (nuID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------



#previouse student alumn blueprint routes
@advisor.route('/alumstudent', methods=['GET'])
def get_all_connections():
    """
    Retrieve all student-alumni connections.
    """
    query = "SELECT nuID, alumID FROM AlumStudent ORDER BY nuID"  # Fetch specific columns to avoid ambiguity
    current_app.logger.info(f"GET /alumstudent query: {query}")
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
    
# Add a new alum-student connection
@advisor.route('/alumstudent', methods=['POST'])
def add_alum_student_connection():
    """
    Add a new alum-student connection.
    """
    current_app.logger.info('POST /alumstudent route')

    try:
        # Parse JSON payload
        the_data = request.json
        current_app.logger.info(f"Data received: {the_data}")

        if not the_data:
            current_app.logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400

        # Extract the student and alumni IDs
        student_id = the_data.get("nuID")
        alumni_id = the_data.get("alumID")

        # Log the received data
        current_app.logger.info(f"Adding connection: Student ID: {student_id}, Alumni ID: {alumni_id}")

        # Validate the input data
        if not student_id or not alumni_id:
            error_message = "Student ID and Alumni ID are required."
            current_app.logger.error(error_message)
            return jsonify({"error": error_message}), 400

        # Prepare the SQL query
        query = '''
            INSERT INTO AlumStudent (nuID, alumID)
            VALUES (%s, %s)
        '''
        data = (student_id, alumni_id)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
        
        current_app.logger.info("Connection added successfully.")
        return jsonify({
            "message": f"Connection between Student ID {student_id} and Alumni ID {alumni_id} added successfully.",
            "student_id": student_id,
            "alumni_id": alumni_id
        }), 201

    except Exception as e:
        # Log the error and return a failure response
        current_app.logger.error(f"Error adding connection: {str(e)}")
        return jsonify({
            "error": f"Failed to add connection: {str(e)}",
            "error_type": type(e).__name__
        }), 500


#Student
@advisor.route('/alumstudent/<nuID>', methods=['GET'])
def get_alum_connections(nuID):
    """
    Retrieve all alumni connections for a specific student.
    """
    current_app.logger.info(f'GET /alumstudent/{nuID} route')

    query = '''
        SELECT a.firstName, 
               a.lastName,
               a.email,
               a.company,
               a.city
        FROM Alumni a
        JOIN AlumStudent ast ON a.alumID = ast.alumID
        WHERE ast.nuID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (nuID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@advisor.route('/alumstudent/<nuID>/<alumID>', methods=['DELETE'])
def delete_connection(nuID, alumID):
    """
    Delete a specific student-alumni connection.
    """
    # Enhanced logging for debugging
    current_app.logger.info('='*50)
    current_app.logger.info('DELETE REQUEST DETAILS:')
    current_app.logger.info(f'Route: /alumstudent/{nuID}/{alumID}')
    current_app.logger.info(f'Full URL: {request.url}')
    current_app.logger.info(f'Method: {request.method}')
    current_app.logger.info(f'Headers: {dict(request.headers)}')
    current_app.logger.info('='*50)

    try:
        # Log the SQL query for debugging
        query = '''
            DELETE FROM AlumStudent 
            WHERE nuID = %s AND alumID = %s
        '''
        current_app.logger.info(f'Executing SQL query: {query}')
        current_app.logger.info(f'With parameters: nuID={nuID}, alumID={alumID}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (nuID, alumID))
        
        # Log the result of the execution
        current_app.logger.info(f'Rows affected: {cursor.rowcount}')
        
        if cursor.rowcount == 0:
            current_app.logger.warning("No connection found to delete")
            return make_response(jsonify({"error": "Connection not found"}), 404)
        
        db.get_db().commit()
        current_app.logger.info("Connection deleted successfully")
        
        response = make_response(jsonify({
            "message": f"Connection between Student ID {nuID} and Alumni ID {alumID} removed successfully"
        }), 200)
        
        # Log the response being sent
        current_app.logger.info(f'Sending response: {response.get_data(as_text=True)}')
        return response

    except Exception as e:
        current_app.logger.error('='*50)
        current_app.logger.error('ERROR DETAILS:')
        current_app.logger.error(f'Error Type: {type(e).__name__}')
        current_app.logger.error(f'Error Message: {str(e)}')
        current_app.logger.error('='*50)
        
        return make_response(jsonify({
            "error": f"Failed to delete connection: {str(e)}",
            "error_type": type(e).__name__
        }), 500)
    

@advisor.route('/studentalumn/<alumnID>', methods=['GET'])
def get_student_connections(alumnID):
    """
    Retrieve all alumni connections for a specific student.
    """
    current_app.logger.info(f'GET /studentalumn/{alumnID} route')

    query = '''
        SELECT s.firstName, 
               s.lastName,
               s.email,
               s.company,
               s.city
        FROM Student s
        JOIN AlumStudent ast ON s.nuID = ast.nuID
        WHERE ast.alumID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (alumnID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@advisor.route('/studentAlumni/<student_id>/<alumni_id>/<old_alumni_id>', methods=['PUT'])
def update_student_alumni(student_id, alumni_id, old_alumni_id):
    """
    Update the alumniID for a specific student
    """
    current_app.logger.info(f'PUT /student/{student_id}/alumni/{alumni_id}/{old_alumni_id} route')

    
    # SQL query to update the alumniID for the student
    query = '''
        UPDATE AlumStudent   
        SET alumID = %s
        WHERE nuID = %s AND alumID = %s
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (alumni_id, student_id, old_alumni_id))
    db.get_db().commit()

    if cursor.rowcount == 0:
        return make_response(jsonify({
            "error": "Student not found or no changes made"
        }), 404)

    return make_response(jsonify({
        "message": f"Successfully updated student {student_id} with alumni {alumni_id}"}), 200)


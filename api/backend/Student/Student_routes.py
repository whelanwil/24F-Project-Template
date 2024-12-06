from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
student = Blueprint('student', __name__)

# ------------------------------------------------------------
# Retrieve a list of available apartments in the city
@student.route('/apartment/city/<city>', methods=['GET'])
def find_city_housing(city):
    query = '''
        SELECT al.firstName, al.lastName, al.email, ap.*
        FROM Apartment ap
        JOIN Alumni al ON ap.alumID = al.alumID
        WHERE ap.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (city,))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



# Retrieve a list of students in the city
@student.route('/student/city/<city>', methods=['GET'])
def find_city_students(city):
    query = '''
        SELECT s.firstName, s.lastName, s.email, s.company
        FROM Student s
        WHERE s.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (city,))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Retrieve a list of alumni in the city
@student.route('/alumni/city/<city>', methods=['GET'])
def find_city_alumni(city):
    query = '''
        SELECT a.firstName, a.lastName, a.email, a.company
        FROM Alumni a
        WHERE a.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (city,))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# 3.3 Add a new city that the student is willing to live in
@student.route('/student', methods=['POST'])
def add_new_city():
    
    the_data = request.json
    city = the_data.get('city')
    current_app.logger.info(the_data)

    if not city:
        current_app.logger.error("City is missing from the request body")
        response = make_response("City is required")
        response.status_code = 400
        return response
    
    query = f'''
        INSERT INTO Student (city)
        VALUES (%s)
    '''
   
    current_app.logger.info(f'POST /student query: {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query, (city,))
    db.get_db().commit()
    
    current_app.logger.info("City successfully added")
    response = make_response("Successfully added city")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# 3.5 Update student info including major, company, & city
@student.route('/student/<nuID>', methods=['PUT'])
def update_student_info(nuID):
    current_app.logger.info('PUT /student/{nuID} route')

    the_data = request.json
    current_app.logger.info(f"Data received: {the_data}")

    major = the_data['major']
    company = the_data['company']
    city = the_data['city']

    current_app.logger.info(f"Updating studentID: {nuID} with Major: {major}, Company: {company}, City: {city}")

    query = '''
        UPDATE Student SET major = %s, company = %s, city = %s 
        WHERE nuID = %s
    '''
    data = (major, company, city, nuID)

    try: 
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
        current_app.logger.info("Update successful.")
        return 'Student information updated'
    except Exception as e:
        current_app.logger.error(f"Error updating student info: {e}")
        return f"Failed to update student information: {str(e)}", 500

# ------------------------------------------------------------
# 3.5 Gets all student information based on nuID
@student.route('/student/<nuID>', methods=['GET'])
def get_student_info(nuID):
    current_app.logger.info('GET /student/{nuID} route')

    query = '''
        SELECT firstName, 
               lastName, 
               major, 
               company,
               city
        FROM Student
        WHERE nuID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (nuID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Revoke parent access
@student.route('/student/parent/<parentID>', methods=['DELETE'])
def remove_parent(parentID):
    current_app.logger.info(f'DELETE /student/parent/{parentID} route')
    
    the_data = request.json
    student_id = the_data.get('studentID')
    
    if not student_id:
        return make_response('StudentID is required', 400)

    # First delete from the association table
    association_query = '''
        DELETE FROM StudentParent 
        WHERE parentID = %s AND studentID = %s
    '''
    
    # Then delete from the Parent table
    parent_query = '''
        DELETE FROM Parent 
        WHERE parentID = %s
    '''
    
    try:
        cursor = db.get_db().cursor()
        # Remove the association first
        cursor.execute(association_query, (parentID, student_id))
        # Then remove the parent
        cursor.execute(parent_query, (parentID,))
        db.get_db().commit()

        response = make_response('Parent successfully removed')
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error removing parent: {str(e)}")
        return make_response(f"Failed to remove parent: {str(e)}", 500)

# ------------------------------------------------------------
# Remove a city from the list of cities the student may want to live in
@student.route('/student', methods=['DELETE'])
def remove_city():
    current_app.logger.info('DELETE /student route')

    query = '''
        DELETE FROM Student 
        WHERE city = %s
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response('City removed.')
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Add a new parent for a student
@student.route('/student/parent', methods=['POST'])
def add_parent():
    try:
        the_data = request.json
        current_app.logger.info(the_data)

        # Extract all required data
        student_id = the_data.get('studentID')
        first_name = the_data.get('firstName')
        last_name = the_data.get('lastName')
        email = the_data.get('email')
        phone = the_data.get('phone')
        relationship = the_data.get('relationshipToStudent')

        # Validate required fields
        if not all([student_id, relationship, first_name, last_name, email]):
            return make_response(jsonify({
                "error": "Missing required fields. Please provide all required information."
            }), 400)

        # First insert into Parent table with all fields
        parent_query = '''
            INSERT INTO Parent (firstName, lastName, email, phone, relationshipToStudent)
            VALUES (%s, %s, %s, %s, %s)
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(parent_query, (first_name, last_name, email, phone, relationship))
        parent_id = cursor.lastrowid

        # Then create association in StudentParent table
        association_query = '''
            INSERT INTO StudentParent (studentID, parentID)
            VALUES (%s, %s)
        '''
        cursor.execute(association_query, (student_id, parent_id))
        db.get_db().commit()

        return make_response(jsonify({
            "message": "Parent added successfully",
            "parentID": parent_id
        }), 201)

    except Exception as e:
        current_app.logger.error(f"Error adding parent: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# ------------------------------------------------------------
# Get all parents for a student
@student.route('/student/parents/<studentID>', methods=['GET'])
def get_student_parents(studentID):
    query = '''
        SELECT p.parentID, p.firstName, p.lastName, p.email, p.phone, p.relationshipToStudent
        FROM Parent p
        JOIN StudentParent sp ON p.parentID = sp.parentID
        WHERE sp.studentID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (studentID,))
    parents = cursor.fetchall()
    response = make_response(jsonify(parents))
    response.status_code = 200
    return response


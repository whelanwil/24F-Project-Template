from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
student = Blueprint('student', __name__)

# ------------------------------------------------------------
# Retrieve a list of available apartments in the city
@student.route('/student', methods=['GET'])
def find_city_housing():
    query = '''
        SELECT *
        FROM Apartment ap
        WHERE ap.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Retrieve a list of recommednations in specific location
# @student.route('/student', methods=['GET'])
# def find_loc_recs():
    query = '''
        SELECT r.establishment, r.category, r.location, r.priceRating
        FROM Recommendation r
        WHERE r.location = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Retrieve a list of students in the city
@student.route('/student', methods=['GET'])
def find_city_students():
    query = '''
        SELECT s.firstName, s.lastName, s.email, s.company
        FROM Student s
        WHERE s.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Retrieve a list of alumni in the city
@student.route('/student', methods=['GET'])
def find_city_alumni():
    query = '''
        SELECT a.firstName, a.lastName, a.email, a.company
        FROM Alumni a
        WHERE a.city = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
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
    theData = cursor.fetchone()

    if theData:
        student_info = {
            "firstName": theData[0],
            "lastName": theData[1],
            "major": theData[2],
            "company": theData[3],
            "city": theData[4],
        }
        response = make_response(jsonify(student_info))
        response.status_code = 200
    else: 
        response = make_response(jsonify({"error": "Student not found"}))
        response.status_code = 404

    return response

# ------------------------------------------------------------
# Revoke parent access
@student.route('/student', methods=['DELETE'])
def remove_parent():
    current_app.logger.info('DELETE /student route')

    query = '''
        DELETE FROM Parent 
        WHERE parentID IN (
            SELECT parentID
            FROM StudentParent
            WHERE studentID = %s)
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(f'Parent removed.')
    response.status_code = 200
    return response

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

        # Extract required data
        student_id = the_data.get('nuID')
        parent_first_name = the_data.get('firstName')
        parent_last_name = the_data.get('lastName')
        parent_email = the_data.get('email')
        parent_phone = the_data.get('phone')

        # Validate required fields
        if not all([student_id, parent_first_name, parent_last_name, parent_email]):
            return make_response(jsonify({
                "error": "Missing required fields. Please provide nuID, firstName, lastName, and email"
            }), 400)

        # First insert into Parent table
        parent_query = '''
            INSERT INTO Parent (firstName, lastName, email, phone)
            VALUES (%s, %s, %s, %s)
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(parent_query, (parent_first_name, parent_last_name, parent_email, parent_phone))
        parent_id = cursor.lastrowid

        # Then create association in StudentParent table
        association_query = '''
            INSERT INTO StudentParent (nuID, parentID)
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
@student.route('/student/<nuID>/parents', methods=['GET'])
def get_student_parents(nuID):
    try:
        query = '''
            SELECT p.parentID, p.firstName, p.lastName, p.email, p.phone
            FROM Parent p
            JOIN StudentParent sp ON p.parentID = sp.parentID
            WHERE sp.nuID = %s
        '''

        cursor = db.get_db().cursor()
        cursor.execute(query, (nuID,))
        parents = cursor.fetchall()

        if parents:
            parents_list = [{
                "parentID": parent[0],
                "firstName": parent[1],
                "lastName": parent[2],
                "email": parent[3],
                "phone": parent[4]
            } for parent in parents]
            
            return make_response(jsonify({
                "message": "Parents retrieved successfully",
                "parents": parents_list
            }), 200)
        else:
            return make_response(jsonify({
                "message": "No parents found for this student",
                "parents": []
            }), 200)

    except Exception as e:
        current_app.logger.error(f"Error retrieving parents: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
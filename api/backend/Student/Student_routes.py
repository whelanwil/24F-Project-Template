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
@student.route('/student', methods=['GET'])
def find_loc_recs():
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

    current_app.logger.info(f"Updating studentID: {nuID} 
                            with Major: {major}, Company: {company}, City: {city}")

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
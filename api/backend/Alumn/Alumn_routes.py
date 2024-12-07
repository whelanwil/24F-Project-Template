from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
alumni = Blueprint('alumni', __name__)

# ------------------------------------------------------------
# 1.1 Add new apartment listing to the site for this alumni
@alumni.route('/alumni', methods=['POST'])
def add_new_housing():
    
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    alumID = the_data['alumID']
    beds = the_data['bed']
    baths = the_data['baths']
    rent = the_data['rent']
    description = the_data['description']
    dateAvailableFrom = the_data['dateAvailableFrom']
    dateAvailableTo = the_data['dateAvailableTo']
    street = the_data['street']
    city = the_data['city']
    state = the_data['state']
    country = the_data['country']

    
    query = '''
        INSERT INTO Apartment (alumID, beds, baths, rent, description,
            dateAvailableFrom, dateAvailableTo,
            street, city, state, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (alumID, beds, baths, rent, description, 
              dateAvailableFrom, dateAvailableTo,
              street, city, state, country)
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    
    response = make_response("Successfully added housing")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# 1.1 Update mutable attributes of apartmentID
@alumni.route('/alumni', methods=['PUT'])
def update_housing():
    current_app.logger.info('PUT /alumni route')
    the_data = request.json
    beds = the_data['bed']
    baths = the_data['baths']
    rent = the_data['rent']
    description = the_data['description']
    dateAvailableFrom = the_data['dateAvailableFrom']
    dateAvailableTo = the_data['dateAvailableTo']
    street = the_data['street']
    city = the_data['city']
    state = the_data['state']
    country = the_data['country']
    housing_id = the_data['housingID']

    query = '''
        UPDATE Apartment SET beds = %s, baths = %s, rent = %s, description = %s, 
        dateAvailableFrom = %s, dateAvailableTo = %s,
        street = %s, city = %s, state = %s, country = %s
        WHERE housingID = %s
    '''
    data = (beds, baths, rent, description, dateAvailableFrom, dateAvailableTo, 
            street, city, state, country, housing_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Housing updated'

# ------------------------------------------------------------
# 1.1 Mark the alumni's apartment as no longer available
@alumni.route('/alumni/<housing_id>', methods=['DELETE'])
def delete_housing(housing_id):
    current_app.logger.info(f'DELETE /alumni/{housing_id} route')

    query = '''
        DELETE FROM Apartment 
        WHERE housingID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (housing_id,))
    db.get_db().commit()

    response = make_response(f'Housing {housing_id} deleted.')
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Get housing details for specific alumni
@alumni.route('/alumni/housing/<alum_id>', methods=['GET'])
def get_alumni_housing(alum_id):
    query = '''
        SELECT 
            a.housingID,
            a.beds,
            a.baths,
            a.rent,
            a.description,
            a.dateAvailableFrom as dateAvailableFrom,
            a.dateAvailableTo as dateAvailableTo,
            a.street,
            a.city,
            a.state,
            a.country,
            al.firstName,
            al.lastName,
            al.email
        FROM Apartment a
        JOIN Alumni al ON a.alumID = al.alumID
        WHERE a.alumID = %s
    '''
    
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (alum_id,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
    

@alumni.route('/studentalumn/<alumnID>', methods=['GET'])
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
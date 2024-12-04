from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
alumni = Blueprint('alumni', __name__)

# ------------------------------------------------------------
# Add new apartment listing to the site for this alumni
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

    
    query = f'''
        INSERT INTO Apartment (alumID, beds, bath, rent, description,
            dateAvailableFrom, dateAvailableTo,
            street, city, state, country)
        VALUES ('{alumID}', '{beds}', '{baths}', str({rent}), '{description}',
        '{dateAvailableFrom}', '{dateAvailableTo}', 
        '{street}', '{city}', '{state}', '{country}')
    '''
   
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added housing")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Update mutable attributes of apartmentID
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

    query = '''
        UPDATE Apartment SET beds = %s, baths = %s, rent = %s, description = %s, 
        dateAvailableFrom = %s, dateAvailableTo = %s,
        street = %s, city = %s, state = %s, country = %s
        WHERE housingID = %s
    '''
    data = (beds, baths, rent, description, dateAvailableFrom, dateAvailableTo, street, city, state, country)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Housing updated'

# ------------------------------------------------------------
# Mark the alumni's apartment as no longer available
@alumni.route('/alumni', methods=['DELETE'])
def delete_housing():
    current_app.logger.info('DELETE /alumni route')

    query = '''
        DELETE FROM Apartment 
        WHERE housingID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(f'Housing deleted.')
    response.status_code = 200
    return response
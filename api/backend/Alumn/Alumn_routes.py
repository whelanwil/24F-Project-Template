alumni = Blueprint('alumni', __name__)

@alumni.route('/alumni', methods=['POST'])
def add_new_housing():
    
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
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
student = Blueprint('student', __name__)

@student.route('/student', methods=['POST'])
def add_new_city():
    
    the_data = request.json
    current_app.logger.info(the_data)

    city = the_data['city']
    
    query = f'''
        INSERT INTO Student (city)
        VALUES ('{city}')
    '''
   
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added city")
    response.status_code = 200
    return response

@student.route('/student', methods=['PUT'])
def update_student_info():
    current_app.logger.info('PUT /student route')

    the_data = request.json
    company = the_data['company']
    city = the_data['city']
    advisorID = the_data['advisorID']

    query = '''
        UPDATE Student SET company = %s, city = %s, rent = %s, advisorID = %s, 
        WHERE nuID = %s
    '''
    data = (company, city, advisorID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Student information updated'
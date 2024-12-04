from flask import Flask, request, jsonify, make_response
from datetime import datetime
from flask import Blueprint
from flask import current_app
from backend.db_connection import db

admin = Flask('admin', __name__)

# 2.1
# GET: Retrieve all system updates
@admin.route('/systemAdministrator/update', methods=['GET'])
def get_all_updates():

    query = '''
        SELECT updateID, updateName, updateDescription, timeStamp, adminID
        FROM Updates
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        updates = cursor.fetchall()

        results = [
            {
                "update_id": row[0],
                "title": row[1],
                "description": row[2],
                "created_at": row[3],
                "admin_id": row[4],
            }
            for row in updates
        ]

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# POST: Create a new system update 
@admin.route('/systemAdministrator/update', methods=['POST'])
def create_update():
    data = request.json
    title = data.get('updateName')
    description = data.get('updateDescription')
    admin_id = data.get('adminID')

    if not title or not description:
        return make_response(jsonify({"error": "Title and description are required"}), 400)

    query = '''
        INSERT INTO Updates (updateName, updateDescription, timeStamp, adminID)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        now = datetime.utcnow()
        cursor.execute(query, (title, description, now, admin_id))
        db.get_db().commit()
        return make_response(jsonify({"message": "System update created successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

# PUT: Modify an existing system update
@admin.route('/systemAdministrator/update/<int:update_id>', methods=['PUT'])
def update_system_update(update_id):
    data = request.json
    title = data.get('updateName')
    description = data.get('updateDescription')

    if not title or not description:
        return make_response(jsonify({"error": "Title and description are required"}), 400)

    query = '''
        UPDATE Updates
        SET updateName = %s, updateDescription = %s, timeStamp = %s
        WHERE updateID = %s
    '''
    try:
        cursor = db.get_db().cursor()
        now = datetime.utcnow()
        cursor.execute(query, (title, description, now, update_id))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Update ID not found"}), 404)

        return make_response(jsonify({"message": "System update modified successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
#2.4 
# Post: Add alumni to database
@admin.route('/systemAdministrator/alumni', methods=['POST'])
def add_alumni():
    """
    Add a new alumni to the database.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    # Validate required fields
    if not all([first_name, last_name, email]):
        return make_response(
            jsonify({"error": "First name, last name, and email"}), 
            400
        )

    # SQL query to insert a new alumni record
    query = '''
        INSERT INTO Alumni (firstName, lastName, email)
        VALUES (%s, %s, %s)
    '''
    try:
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email))
        db.get_db().commit()

        # Success response
        return make_response(
            jsonify({"message": "Alumni added successfully"}), 
            201
        )

    except Exception as e:
        # Log and handle errors
        print(f"Error occurred: {e}")
        return make_response(
            jsonify({"error": "An internal server error occurred"}), 
            500
        )

# PUT: Update an alumni's information
@admin.route('/systemAdministrator/alumni/<int:alum_id>', methods=['PUT'])
def update_alumni(alum_id):
    """
    Update an alumni's information in the database.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return make_response(jsonify({"error": "First name, last name, email, and graduation year are required"}), 400)

    query = '''
        UPDATE Alumni
        SET firstName = %s, lastName = %s, email = %s
        WHERE alumID = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, alum_id))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Alumni not found or is inactive"}), 404)

        return make_response(jsonify({"message": "Alumni information updated successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
#2.6
# add co op advior instead maybe
@admin.route('/systemAdministrator/student', methods=['POST'])
def add_student_with_city():
    """
    Add a new student to the database.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    company = data.get('company')
    city = data.get('city')
    admin_id = data.get('adminID')
    advisor_id = data.get('advisorID')

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
            jsonify({"message": f"Student '{first_name} {last_name}' added successfully"}), 
            201
        )

    except Exception as e:
        # Log and handle errors
        print(f"Error occurred: {e}")
        return make_response(jsonify({"error": "An internal server error occurred"}), 500)
    
@admin.route('/systemAdministrator/student/<string:city>', methods=['DELETE'])
def delete_relevant_city(city):
    """
    Remove a city from the database.
    """
    query = '''
        DELETE FROM Student
        WHERE city = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": f"City '{city}' not found"}), 404)

        return make_response(jsonify({"message": f"City '{city}' removed successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
if __name__ == '__main__':
    admin.run(debug=True)
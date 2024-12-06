import datetime
from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
admin = Blueprint('admin', __name__)

# ------------------------------------------------------------
# 2.1 Get all system updates
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
    
# ------------------------------------------------------------
# 2.1 Create a new system update record with details
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

# ------------------------------------------------------------
# 2.1 Modify an existing system update with new information
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
    
# ------------------------------------------------------------ 
# 2.4 Add a new alumni to the database
@admin.route('/systemAdministrator/alumni', methods=['POST'])
def add_alumni():
    """
    Add a new alumni to the database with all available fields.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    major = data.get('major')
    email = data.get('email')
    company = data.get('company')
    city = data.get('city')
    admin_id = data.get('adminID')

    # Validate required fields
    if not all([first_name, last_name, major, email, admin_id]):
        return make_response(
            jsonify({"error": "First name, last name, major, email, and adminID are required"}), 
            400
        )

    # SQL query to insert a new alumni record with all fields
    query = '''
        INSERT INTO Alumni (firstName, lastName, major, email, company, city, adminID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            first_name, 
            last_name, 
            major,
            email, 
            company, 
            city, 
            admin_id
        ))
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

# ------------------------------------------------------------ 
# 2.4 Update an alumni's information
@admin.route('/systemAdministrator/alumni/<alumID>', methods=['PUT'])
def update_alumni(alumID):
    """
    Update an alumni's information in the database.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    company = data.get('company')
    city = data.get('city')

    if not all([first_name, last_name, email]):
        return make_response(jsonify({"error": "First name, last name, and email are required"}), 400)

    query = '''
        UPDATE Alumni
        SET firstName = %s, lastName = %s, email = %s, company = %s, city = %s
        WHERE alumID = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, company, city, alumID))
        db.get_db().commit()
    
        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Alumni not found"}), 404)

        return make_response(jsonify({"message": "Alumni information updated successfully"}), 200)
    except Exception as e:
        print(f"Error occurred: {e}")
        return make_response(jsonify({"error": str(e)}), 500)
    
#get all alumni
@admin.route('/systemAdministrator/alumni', methods=['GET'])
def get_all_alumni():
    query = '''
        SELECT * FROM Alumni
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#get all students
@admin.route('/systemAdministrator/student', methods=['GET'])
def get_all_students():
    query = '''
        SELECT * FROM Student
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#get all advisors
@admin.route('/systemAdministrator/advisor', methods=['GET'])
def get_all_advisors():
    query = '''
        SELECT * FROM CoopAdvisor
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------ 
# 2.3 Add a new student to the database
@admin.route('/systemAdministrator/student', methods=['POST'])
def add_student():
    """
    Add a new student to the database with all required fields.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    major = data.get('major')
    email = data.get('email')
    company = data.get('company')
    city = data.get('city')
    admin_id = data.get('adminID')
    advisor_id = data.get('advisorID')

    # Validate required fields based on SQL schema
    if not all([first_name, last_name, major, admin_id, advisor_id]):
        return make_response(
            jsonify({"error": "First name, last name, major, adminID, and advisorID are required"}), 
            400
        )

    # SQL query to insert a new student record
    query = '''
        INSERT INTO Student (firstName, lastName, major, email, company, city, adminID, advisorID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            first_name,
            last_name,
            major,
            email,
            company,
            city,
            admin_id,
            advisor_id
        ))
        db.get_db().commit()
        return make_response(
            jsonify({"message": "Student added successfully"}), 
            201
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return make_response(
            jsonify({"error": "An internal server error occurred"}), 
            500
        )

@admin.route('/systemAdministrator/advisor', methods=['POST'])
def add_advisor():
    """
    Add a new advisor to the database with all required fields.
    """
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    admin_id = data.get('adminID')

    # Validate required fields based on SQL schema
    if not all([first_name, last_name, admin_id]):
        return make_response(
            jsonify({"error": "First name, last name, and adminID are required"}), 
            400
        )

    # SQL query to insert a new advisor record
    query = '''
        INSERT INTO CoopAdvisor (firstName, lastName, email, adminID)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            first_name,
            last_name,
            email,
            admin_id
        ))
        db.get_db().commit()
        return make_response(
            jsonify({"message": "Advisor added successfully"}), 
            201
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return make_response(
            jsonify({"error": "An internal server error occurred"}), 
            500
        )

from flask import Flask, request, jsonify, make_response
from datetime import datetime

app = Flask(__name__)

# 2.1
# GET: Retrieve all system updates
@app.route('/systemAdministrator/update', methods=['GET'])
def get_all_updates():
    query = '''
        SELECT update_id, title, description, created_at, updated_at
        FROM system_updates
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
                "updated_at": row[4],
            }
            for row in updates
        ]

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# POST: Create a new system update record
@app.route('/systemAdministrator/update', methods=['POST'])
def create_update():
    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return make_response(jsonify({"error": "Title and description are required"}), 400)

    query = '''
        INSERT INTO system_updates (title, description, created_at, updated_at)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        now = datetime.utcnow()
        cursor.execute(query, (title, description, now, now))
        db.get_db().commit()
        return make_response(jsonify({"message": "System update created successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

# PUT: Modify an existing system update
@app.route('/systemAdministrator/update/<int:update_id>', methods=['PUT'])
def update_system_update(update_id):
    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return make_response(jsonify({"error": "Title and description are required"}), 400)

    query = '''
        UPDATE system_updates
        SET title = %s, description = %s, updated_at = %s
        WHERE update_id = %s
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

# DELETE: Remove a specific system update record
@app.route('/systemAdministrator/update/<int:update_id>', methods=['DELETE'])
def delete_system_update(update_id):
    query = '''
        DELETE FROM system_updates
        WHERE update_id = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (update_id,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Update ID not found"}), 404)

        return make_response(jsonify({"message": "System update deleted successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

if __name__ == '__main__':
    app.run(debug=True)

# 2.2
@app.route('/systemAdministrator/performance/<int:metric_id>', methods=['GET'])
def get_performance_metrics(metric_id):
    """
    Retrieve a list of performance metrics for a specific metric ID.
    """
    query = '''
        SELECT 
            metric_id,
            metric_name,
            metric_value,
            recorded_at
        FROM 
            performance_metrics
        WHERE 
            metric_id = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (metric_id,))
        metrics = cursor.fetchall()

        # Format the results into a JSON-friendly structure
        results = [
            {
                "metric_id": row[0],
                "metric_name": row[1],
                "metric_value": row[2],
                "recorded_at": row[3]
            }
            for row in metrics
        ]

        if not results:
            return make_response(jsonify({"error": "No metrics found for the given metric ID"}), 404)

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# 2.3
# GET: Retrieve a list of all active students or specific student by ID
@app.route('/systemAdministrator/student/<int:student_id>', methods=['GET'])
def get_students(student_id):
    """
    Retrieve a list of all active students or specific student information by ID.
    """
    try:
        cursor = db.get_db().cursor()
        
        if student_id == 0:  # Retrieve all active students
            query = '''
                SELECT 
                    student_id, 
                    first_name, 
                    last_name, 
                    email, 
                    enrolled_at 
                FROM 
                    students 
                WHERE 
                    is_active = 1
            '''
            cursor.execute(query)
        else:  # Retrieve a specific student by ID
            query = '''
                SELECT 
                    student_id, 
                    first_name, 
                    last_name, 
                    email, 
                    enrolled_at 
                FROM 
                    students 
                WHERE 
                    student_id = %s AND is_active = 1
            '''
            cursor.execute(query, (student_id,))

        students = cursor.fetchall()
        
        # Format the results into a JSON-friendly structure
        results = [
            {
                "student_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "enrolled_at": row[4]
            }
            for row in students
        ]

        if not results:
            return make_response(jsonify({"error": "No active students found"}), 404)

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    

# POST: Add a new student to the database
@app.route('/systemAdministrator/student', methods=['POST'])
def add_student():
    """
    Add a new student to the database.
    """
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return make_response(jsonify({"error": "First name, last name, and email are required"}), 400)

    query = '''
        INSERT INTO students (first_name, last_name, email, is_active, enrolled_at)
        VALUES (%s, %s, %s, 1, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        enrolled_at = datetime.utcnow()
        cursor.execute(query, (first_name, last_name, email, enrolled_at))
        db.get_db().commit()

        return make_response(jsonify({"message": "Student added successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# PUT: Update a student's information
@app.route('/systemAdministrator/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update a student's information in the database.
    """
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return make_response(jsonify({"error": "First name, last name, and email are required"}), 400)

    query = '''
        UPDATE students
        SET first_name = %s, last_name = %s, email = %s
        WHERE student_id = %s AND is_active = 1
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, student_id))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Student not found or is inactive"}), 404)

        return make_response(jsonify({"message": "Student information updated successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
#2.4
# GET: Retrieve a list of all active alumni or specific alumni by ID
@app.route('/systemAdministrator/alumni/<int:alum_id>', methods=['GET'])
def get_alumni(alum_id):
    """
    Retrieve a list of all active alumni or specific alumni information by ID.
    """
    try:
        cursor = db.get_db().cursor()
        
        if alum_id == 0:  # Retrieve all active alumni
            query = '''
                SELECT 
                    alum_id, 
                    first_name, 
                    last_name, 
                    email, 
                    graduation_year 
                FROM 
                    alumni 
                WHERE 
                    is_active = 1
            '''
            cursor.execute(query)
        else:  # Retrieve a specific alumni by ID
            query = '''
                SELECT 
                    alum_id, 
                    first_name, 
                    last_name, 
                    email, 
                    graduation_year 
                FROM 
                    alumni 
                WHERE 
                    alum_id = %s AND is_active = 1
            '''
            cursor.execute(query, (alum_id,))

        alumni = cursor.fetchall()
        
        # Format the results into a JSON-friendly structure
        results = [
            {
                "alum_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "graduation_year": row[4]
            }
            for row in alumni
        ]

        if not results:
            return make_response(jsonify({"error": "No active alumni found"}), 404)

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# POST: Add a new alumni to the database
@app.route('/systemAdministrator/alumni', methods=['POST'])
def add_alumni():
    """
    Add a new alumni to the database.
    """
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    graduation_year = data.get('graduation_year')

    if not first_name or not last_name or not email or not graduation_year:
        return make_response(jsonify({"error": "First name, last name, email, and graduation year are required"}), 400)

    query = '''
        INSERT INTO alumni (first_name, last_name, email, graduation_year, is_active)
        VALUES (%s, %s, %s, %s, 1)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, graduation_year))
        db.get_db().commit()

        return make_response(jsonify({"message": "Alumni added successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
# PUT: Update an alumni's information
@app.route('/systemAdministrator/alumni/<int:alum_id>', methods=['PUT'])
def update_alumni(alum_id):
    """
    Update an alumni's information in the database.
    """
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    graduation_year = data.get('graduation_year')

    if not first_name or not last_name or not email or not graduation_year:
        return make_response(jsonify({"error": "First name, last name, email, and graduation year are required"}), 400)

    query = '''
        UPDATE alumni
        SET first_name = %s, last_name = %s, email = %s, graduation_year = %s
        WHERE alum_id = %s AND is_active = 1
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, graduation_year, alum_id))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Alumni not found or is inactive"}), 404)

        return make_response(jsonify({"message": "Alumni information updated successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
#2.5
@app.route('/systemAdministrator/coopAdvisor/<int:advisor_id>', methods=['GET'])
def get_coop_advisors(advisor_id):
    """
    Retrieve a list of all co-op advisors or specific advisor information by ID.
    """
    try:
        cursor = db.get_db().cursor()

        if advisor_id == 0:  # Retrieve all co-op advisors
            query = '''
                SELECT 
                    advisor_id, 
                    first_name, 
                    last_name, 
                    email, 
                    department 
                FROM 
                    coop_advisors
            '''
            cursor.execute(query)
        else:  # Retrieve a specific advisor by ID
            query = '''
                SELECT 
                    advisor_id, 
                    first_name, 
                    last_name, 
                    email, 
                    department 
                FROM 
                    coop_advisors 
                WHERE 
                    advisor_id = %s
            '''
            cursor.execute(query, (advisor_id,))

        advisors = cursor.fetchall()

        # Format the results into a JSON-friendly structure
        results = [
            {
                "advisor_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "department": row[4]
            }
            for row in advisors
        ]

        if not results:
            return make_response(jsonify({"error": "No co-op advisors found"}), 404)

        return make_response(jsonify(results), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
@app.route('/systemAdministrator/coopAdvisor', methods=['POST'])
def add_coop_advisor():
    """
    Add a new co-op advisor to the database.
    """
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    department = data.get('department')

    if not first_name or not last_name or not email or not department:
        return make_response(jsonify({"error": "First name, last name, email, and department are required"}), 400)

    query = '''
        INSERT INTO coop_advisors (first_name, last_name, email, department)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (first_name, last_name, email, department))
        db.get_db().commit()

        return make_response(jsonify({"message": "Co-op advisor added successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)




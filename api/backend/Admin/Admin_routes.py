from flask import Flask, request, jsonify, make_response
from datetime import datetime

app = Flask(__name__)

# 2.1
# GET: Retrieve all system updates
@app.route('/systemAdministrator/update', methods=['GET'])
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
        INSERT INTO Updates (updateName, updateDescription, timeStamp, adminID)
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
        UPDATE Alumni
        SET firstName = %s, lastName = %s, email = %s
        WHERE alumID = %s
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

if __name__ == '__main__':
    app.run(debug=True)
    
#2.4 
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
        UPDATE Alumni
        SET firstName = %s, lastName = %s, email = %s
        WHERE alumID = %s
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
    
#2.6
@app.route('/systemAdministrator/student/city', methods=['POST'])
def add_relevant_city():
    """
    Add a new city to the database.
    """
    data = request.json
    city_name = data.get('city_name')

    if not city_name:
        return make_response(jsonify({"error": "City name is required"}), 400)

    query = '''
        INSERT INTO Student (firstName, lastName, email, company, city, adminID, advisorID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city_name,))
        db.get_db().commit()

        return make_response(jsonify({"message": f"City '{city_name}' added successfully"}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    
@app.route('/systemAdministrator/student/<string:city>', methods=['DELETE'])
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






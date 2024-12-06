from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
studentAlum = Blueprint('studentAlum', __name__)

@studentAlum.route('/alumstudent', methods=['GET'])
def get_all_connections():
    """
    Retrieve all student-alumni connections.
    """
    query = "SELECT nuID, alumID FROM AlumStudent ORDER BY nuID"  # Fetch specific columns to avoid ambiguity
    current_app.logger.info(f"GET /alumstudent query: {query}")
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
    
# Add a new alum-student connection
@studentAlum.route('/alumstudent', methods=['POST'])
def add_alum_student_connection():
    """
    Add a new alum-student connection.
    """
    current_app.logger.info('POST /alumstudent route')

    try:
        # Parse JSON payload
        the_data = request.json
        current_app.logger.info(f"Data received: {the_data}")

        if not the_data:
            current_app.logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400

        # Extract the student and alumni IDs
        student_id = the_data.get("nuID")
        alumni_id = the_data.get("alumID")

        # Log the received data
        current_app.logger.info(f"Adding connection: Student ID: {student_id}, Alumni ID: {alumni_id}")

        # Validate the input data
        if not student_id or not alumni_id:
            error_message = "Student ID and Alumni ID are required."
            current_app.logger.error(error_message)
            return jsonify({"error": error_message}), 400

        # Prepare the SQL query
        query = '''
            INSERT INTO AlumStudent (nuID, alumID)
            VALUES (%s, %s)
        '''
        data = (student_id, alumni_id)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
        
        current_app.logger.info("Connection added successfully.")
        return jsonify({
            "message": f"Connection between Student ID {student_id} and Alumni ID {alumni_id} added successfully.",
            "student_id": student_id,
            "alumni_id": alumni_id
        }), 201

    except Exception as e:
        # Log the error and return a failure response
        current_app.logger.error(f"Error adding connection: {str(e)}")
        return jsonify({
            "error": f"Failed to add connection: {str(e)}",
            "error_type": type(e).__name__
        }), 500


@studentAlum.route('/alumstudent/<nuID>', methods=['GET'])
def get_student_connections(nuID):
    """
    Retrieve all alumni connections for a specific student.
    """
    current_app.logger.info(f'GET /alumstudent/{nuID} route')

    query = '''
        SELECT a.firstName, 
               a.lastName,
               a.email,
               a.company,
               a.city
        FROM Alumni a
        JOIN AlumStudent ast ON a.alumID = ast.alumID
        WHERE ast.nuID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (nuID,))
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@studentAlum.route('/alumstudent/<nuID>/<alumID>', methods=['DELETE'])
def delete_connection(nuID, alumID):
    """
    Delete a specific student-alumni connection.
    """
    # Enhanced logging for debugging
    current_app.logger.info('='*50)
    current_app.logger.info('DELETE REQUEST DETAILS:')
    current_app.logger.info(f'Route: /alumstudent/{nuID}/{alumID}')
    current_app.logger.info(f'Full URL: {request.url}')
    current_app.logger.info(f'Method: {request.method}')
    current_app.logger.info(f'Headers: {dict(request.headers)}')
    current_app.logger.info('='*50)

    try:
        # Log the SQL query for debugging
        query = '''
            DELETE FROM AlumStudent 
            WHERE nuID = %s AND alumID = %s
        '''
        current_app.logger.info(f'Executing SQL query: {query}')
        current_app.logger.info(f'With parameters: nuID={nuID}, alumID={alumID}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (nuID, alumID))
        
        # Log the result of the execution
        current_app.logger.info(f'Rows affected: {cursor.rowcount}')
        
        if cursor.rowcount == 0:
            current_app.logger.warning("No connection found to delete")
            return make_response(jsonify({"error": "Connection not found"}), 404)
        
        db.get_db().commit()
        current_app.logger.info("Connection deleted successfully")
        
        response = make_response(jsonify({
            "message": f"Connection between Student ID {nuID} and Alumni ID {alumID} removed successfully"
        }), 200)
        
        # Log the response being sent
        current_app.logger.info(f'Sending response: {response.get_data(as_text=True)}')
        return response

    except Exception as e:
        current_app.logger.error('='*50)
        current_app.logger.error('ERROR DETAILS:')
        current_app.logger.error(f'Error Type: {type(e).__name__}')
        current_app.logger.error(f'Error Message: {str(e)}')
        current_app.logger.error('='*50)
        
        return make_response(jsonify({
            "error": f"Failed to delete connection: {str(e)}",
            "error_type": type(e).__name__
        }), 500)

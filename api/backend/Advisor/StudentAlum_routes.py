from flask import Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
advisor = Blueprint('studentAlum', __name__)

@advisor.route('/alumstudent', methods=['GET'])
def get_all_connections():
    """
    Retrieve all student-alumni connections.
    """
    query = "SELECT * FROM AlumStudent"  # Query to fetch all connections
    current_app.logger.info(f"GET /alumstudent query: {query}")
    
    try:
        # Connect to the database and execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        connections = cursor.fetchall()
        
        # Log the query results
        current_app.logger.info(f"Query results: {connections}")
        
        # Format the results into a list of dictionaries
        formatted_connections = [{"nuID": row[0], "alumID": row[1]} for row in connections]
        
        # Return the data as a JSON response
        return make_response(
            jsonify({"message": "Data retrieved successfully", "data": formatted_connections}),
            200
        )
    
    except Exception as e:
        # Log the error
        current_app.logger.error(f"Database error: {str(e)}")
        
        # Return an error response
        return make_response(jsonify({"error": str(e)}), 500)
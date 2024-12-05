from flask import Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
studentAlum = Blueprint('studentAlum', __name__)

@studentAlum.route('/alumstudent', methods=['GET'])
def get_all_connections():
    """
    Retrieve all student-alumni connections.
    """
    query = "SELECT nuID, alumID FROM AlumStudent"  # Fetch specific columns to avoid ambiguity
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
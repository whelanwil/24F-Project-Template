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
        # Connect to the database
        db_conn = db.get_db()
        current_app.logger.info("Database connection successful.")

        # Execute the query
        cursor = db_conn.cursor()
        cursor.execute(query)
        connections = cursor.fetchall()
        current_app.logger.info(f"Raw query results: {connections}")  # Log raw results
        
        # If connections is empty, return a friendly response
        if not connections:
            current_app.logger.info("No connections found in AlumStudent table.")
            return jsonify({"message": "No connections found.", "data": []}), 200

        # Debug each row's structure before processing
        for row in connections:
            current_app.logger.info(f"Row structure: {row}")

        # Format the results
        formatted_connections = [{"nuID": row[0], "alumID": row[1]} for row in connections]
        return jsonify({"message": "Data retrieved successfully", "data": formatted_connections}), 200
    except Exception as e:
        current_app.logger.error("Error occurred in /alumstudent route", exc_info=True)
        return jsonify({"error": f"Database error: {str(e)}"}), 500
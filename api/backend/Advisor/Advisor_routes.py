from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
advisor = Blueprint('advisor', __name__)

# ------------------------------------------------------------
# Get all alumni offering housing in a specific city
@advisor.route('/alumni/<city>', methods=['GET'])
def get_alumni_housing():
    query = '''
        SELECT A.alumID
        FROM Alumni A
        JOIN Apartment Ap ON A.alumID = Ap.alumID
        WHERE city = %s
    '''
    
    current_app.logger.info(f'GET /alumni/<city> query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city,))
        theData = cursor.fetchall()
        current_app.logger.info(f'Query Result: {theData}')

        response = make_response(jsonify({"message": "Data retrieved successfully", "data": theData}), 200)
        return response
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

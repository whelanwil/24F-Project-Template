from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
advisor = Blueprint('advisor', __name__)

# ------------------------------------------------------------
# 4.1 Get all alumni offering housing in a specific city
@advisor.route('/alumni/<city>', methods=['GET'])
def get_alumni_housing(city):
    query = '''
        SELECT A.alumID, A.firstName, A.lastName, Ap.city
        FROM Alumni A
        JOIN Apartment Ap ON A.alumID = Ap.alumID
        WHERE A.city = %s
    '''
    
    current_app.logger.info(f'GET /alumni/<city> query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
    

# ------------------------------------------------------------
# Revoke parental access
@advisor.route('/coopAdvisor/communication/parents/<parentID>', methods=['DELETE'])
def revoke_parental_access(parentID):
    current_app.logger.info(f'DELETE /parents/{parentID} route')

    query = '''
        DELETE FROM StudentParent
        WHERE parentID = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (parentID,))
    db.get_db().commit()

    if cursor.rowcount > 0:
        response = make_response(f'Parental access revoked for parent ID {parentID}.')
        response.status_code = 200
    else:
        response = make_response(f'No association found for parent ID {parentID}.')
        response.status_code = 404

    return response

# ------------------------------------------------------------
# Track which students have found housing
@advisor.route('/alumni/<city>', methods=['GET'])
def get_alumni_housing(city):
    query = '''
        SELECT A.alumID, A.firstName, A.lastName, Ap.city
        FROM Alumni A
        JOIN Apartment Ap ON A.alumID = Ap.alumID
        WHERE A.city = %s
    '''
    current_app.logger.info(f'GET /alumni/<city> query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (city,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)
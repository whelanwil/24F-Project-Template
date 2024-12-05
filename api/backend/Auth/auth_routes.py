from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Initialize Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/student/<id>', methods=['GET'])
def get_student(id):
    query = '''
        SELECT firstName, lastName
        FROM Student
        WHERE nuID = %s
    '''
    
    current_app.logger.info(f'GET /student/{id} query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

@auth.route('/advisor/<int:id>', methods=['GET'])
def get_advisor(id):
    query = '''
        SELECT firstName, lastName
        FROM CoopAdvisor
        WHERE advisorID = %s
    '''
    
    current_app.logger.info(f'GET /advisor/{id} query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

@auth.route('/admin/<int:id>', methods=['GET'])
def get_admin(id):
    query = '''
        SELECT firstName, lastName
        FROM SystemAdministrator
        WHERE adminID = %s
    '''
    
    current_app.logger.info(f'GET /admin/{id} query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

@auth.route('/alumni/<int:id>', methods=['GET'])
def get_alumni(id):
    query = '''
        SELECT firstName, lastName
        FROM Alumni
        WHERE alumID = %s
    '''
    
    current_app.logger.info(f'GET /alumni/{id} query: {query}')
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchall()

        current_app.logger.info(f"Query results: {results}")
        return make_response(jsonify({"message": "Data retrieved successfully", "data": results}), 200)
    except Exception as e:
        current_app.logger.error(f"Database error: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

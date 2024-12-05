from flask import Blueprint, request, jsonify
from backend.db_connection import db

# Initialize Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        # Define queries for each role
        queries = {
            "student": "SELECT firstName, lastName, 'student' AS role FROM Student WHERE nuID = %s",
            "alumni": "SELECT firstName, lastName, 'alumni' AS role FROM Alumni WHERE alumID = %s",
            "advisor": "SELECT firstName, lastName, 'advisor' AS role FROM CoopAdvisor WHERE advisorID = %s",
            "admin": "SELECT firstName, lastName, 'administrator' AS role FROM SystemAdministrator WHERE adminID = %s"
        }

        # Iterate over the queries to find which table contains the ID
        for role, query in queries.items():
            cursor = db.get_db().cursor()
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if result:
                return jsonify({
                    "first_name": result[0],
                    "last_name": result[1],
                    "role": role
                }), 200

        # If no result was found, return an error
        return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

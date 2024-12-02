from flask import Flask, request, jsonify, make_response
from datetime import datetime

app = Flask(__name__)

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

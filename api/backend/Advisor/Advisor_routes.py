from flask import Flask, request, jsonify, make_response
from datetime import datetime

advisor = Flask('advisor', __name__)

#------------------------------------------------------------
# 4.1 Get all alumni offering housing in a specific city

@advisor.route('/alumni/<city>', methods=['GET'])
def get_alumni_housing(city):

    query = f'''SELECT A.alumID
                FROM Alumni A
                JOIN Apartment Ap ON A.alumID = Ap.alumID
                WHERE city = '{city}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
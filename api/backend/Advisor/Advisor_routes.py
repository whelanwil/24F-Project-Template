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

# GET: Track which students have found housing by linking the Student and Connect tables to Apartment.
@app.route('/students/housing', methods=['GET'])
def get_students_with_housing():

    query = '''
        SELECT 
            Student.nuID AS student_id,
            Student.firstName AS first_name,
            Student.lastName AS last_name,
            Apartment.housingID AS housing_id,
            Apartment.beds AS number_of_beds,
            Apartment.baths AS number_of_baths,
            Apartment.rent AS rent,
            Apartment.city AS city,
            Apartment.state AS state,
            Apartment.country AS country
        FROM 
            Student
        INNER JOIN AlumStudent ON Student.nuID = AlumStudent.nuID
        INNER JOIN Apartment ON AlumStudent.alumID = Apartment.alumID
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        students_with_housing = [
            {
                "student_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "housing_id": row[3],
                "number_of_beds": row[4],
                "number_of_baths": row[5],
                "rent": row[6],
                "city": row[7],
                "state": row[8],
                "country": row[9],
            }
            for row in results
        ]

        return make_response(jsonify(students_with_housing), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

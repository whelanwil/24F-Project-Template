USE huskyDenDB;

# get 2.1
SELECT updateID, updateName, updateDescription, timeStamp, adminID
        FROM Updates;

# put 2.1
UPDATE Updates
        SET updateName = %s, updateDescription = %s, timeStamp = %s
        WHERE updateID = %s;

# post 2.1
INSERT INTO Updates (updateName, updateDescription, timeStamp, adminID)
        VALUES (%s, %s, %s, %s);

# put 2.4
UPDATE Alumni
    SET firstName = %s, lastName = %s, email = %s
    WHERE alumID = %s;

# post 2.6
INSERT INTO Student (firstName, lastName, email, company, city, adminID, advisorID)
        VALUES (%s, %s, %s, %s, %s, %s, %s);

# delete 2.6
DELETE FROM Student
        WHERE city = %s;

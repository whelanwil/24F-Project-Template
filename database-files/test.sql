DROP DATABASE IF EXISTS `husky-den`;

CREATE DATABASE IF NOT EXISTS `husky-den`;

USE `husky-den`;

SELECT
            a.housingID,
            a.beds,
            a.baths,
            a.rent,
            a.description,
            DATE_FORMAT(a.dateAvailableFrom, '%%Y-%%m-%%d') as dateAvailableFrom,
            DATE_FORMAT(a.dateAvailableTo, '%%Y-%%m-%%d') as dateAvailableTo,
            a.street,
            a.city,
            a.state,
            a.country,
            al.firstName,
            al.lastName,
            al.email
        FROM Apartment a
        JOIN Alumni al ON a.alumID = al.alumID
        WHERE a.alumID = %s;
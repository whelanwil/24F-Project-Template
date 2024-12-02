
DROP DATABASE IF EXISTS huskyDenDB;
CREATE DATABASE huskyDenDB;
USE huskyDenDB;

DROP TABLE IF EXISTS `SystemAdministrator`;
CREATE TABLE `SystemAdministrator` (
    `adminID` INTEGER PRIMARY KEY ,
    `firstName` VARCHAR(50),
    `lastName` VARCHAR(50),
    `email` VARCHAR(75)
);

DROP TABLE IF EXISTS `Alumni`;
CREATE TABLE `Alumni` (
    `alumID` INTEGER PRIMARY KEY,
    `firstName` VARCHAR(50) NOT NULL,
    `lastName` VARCHAR(50) NOT NULL,
    `email` VARCHAR(75),
    `company` VARCHAR(50),
    `city` VARCHAR(50),
    `adminID` INTEGER NOT NULL,
    FOREIGN KEY (`adminID`)
        REFERENCES `SystemAdministrator` (`adminID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `CoopAdvisor`;
CREATE TABLE `CoopAdvisor` (
    `advisorID` INTEGER PRIMARY KEY,
    `firstName` VARCHAR(50) NOT NULL,
    `lastName` VARCHAR(50) NOT NULL,
    `email` VARCHAR(75),
    `adminID` INTEGER NOT NULL,
    FOREIGN KEY (`adminID`)
        REFERENCES `SystemAdministrator` (`adminID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS `Student`;
CREATE TABLE `Student` (
    `nuID` INTEGER PRIMARY KEY,
    `firstName` VARCHAR(50) NOT NULL,
    `lastName` VARCHAR(50) NOT NULL,
    `email` VARCHAR(75),
    `company` VARCHAR(50),
    `city` VARCHAR(75),
    `adminID` INTEGER NOT NULL,
    `advisorID` INTEGER NOT NULL,
    FOREIGN KEY (`adminID`)
        REFERENCES `SystemAdministrator` (`adminID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (`advisorID`)
        REFERENCES `CoopAdvisor` (`advisorID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Parent`;
CREATE TABLE `Parent` (
    `parentID` INTEGER PRIMARY KEY,
    `relationshipToStudent` VARCHAR(50)
);

DROP TABLE IF EXISTS `StudentParent`;
CREATE TABLE `StudentParent` (
    `studentID` INTEGER,
    `parentID` INTEGER,
    PRIMARY KEY (`studentID`, `parentID`),
    FOREIGN KEY (`studentID`)
        REFERENCES `Student` (`nuID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (`parentID`)
        REFERENCES `Parent` (`parentID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Performance`;
CREATE TABLE `Performance` (
    `metricID` INTEGER PRIMARY KEY,
    `metricName` VARCHAR(50),
    `value` INTEGER NOT NULL,
    `timeStamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `adminID` INTEGER NOT NULL,
    FOREIGN KEY (`adminID`)
        REFERENCES `SystemAdministrator`(`adminID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Updates`;
CREATE TABLE `Update` (
    `updateID` INTEGER PRIMARY KEY,
    `updateName` VARCHAR(50),
    `updateDescription` TEXT,
    `timeStamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    `adminID` INTEGER NOT NULL,
    FOREIGN KEY (`adminID`)
        REFERENCES `SystemAdministrator`(`adminID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `AlumAdvisor`;
CREATE TABLE `AlumAdvisor` (
    `alumID` INTEGER NOT NULL,
    `advisorID` INTEGER NOT NULL,
    PRIMARY KEY (`alumID`, `advisorID`),
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni`(`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (`advisorID`)
        REFERENCES `CoopAdvisor` (`advisorID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS `AlumStudent`;
CREATE TABLE `AlumStudent` (
    `nuID` INTEGER NOT NULL,
    `alumID` INTEGER NOT NULL,
    PRIMARY KEY (`nuID`, `alumID`),
    FOREIGN KEY (`nuID`)
        REFERENCES `Student`(`nuID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni` (`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Apartment`;
CREATE TABLE `Apartment` (
    `alumID` INTEGER NOT NULL,
    `housingID` INTEGER NOT NULL AUTO_INCREMENT,
    `beds` INTEGER NOT NULL,
    `baths` INTEGER NOT NULL,
    `rent` INTEGER NOT NULL,
    `description` TEXT,
    `dateAvailableFrom` DATETIME NOT NULL,
    `dateAvailableTo` DATETIME NOT NULL,
    `street` INTEGER NOT NULL,
    `city` VARCHAR(50) NOT NULL,
    `state` VARCHAR(50),
    `country` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`alumID`, `housingID`),
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni` (`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS `Recommendation`;
CREATE TABLE `Recommendation` (
    `alumID` INTEGER NOT NULL,
    `establishment` VARCHAR(75) PRIMARY KEY,
    `category` VARCHAR(75),
    `location` VARCHAR(75),
    `priceRating` INTEGER NOT NULL,
    PRIMARY KEY (`alumID`, `establishment`),
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni` (`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- -- Insert into SystemAdministrator
-- INSERT INTO `SystemAdministrator` (`adminID`, `firstName`, `lastName`, `email`) VALUES
-- (1, 'Jordan', 'Lee', 'jordan.lee@huskyden.com'),
-- (2,'Bob', 'Johnson', 'bob.johnson@huskyden.com');

-- -- Insert into Alumni
-- INSERT INTO `Alumni` (`firstName`, `lastName`, `email`, `company`, `city`, `adminID`) VALUES
-- ('Bridget', 'McCarthy', 'bridget.mccarthy@example.com', 'Apple', 'Los Angeles', 1),
-- ('Dave', 'Wilson', 'dave.wilson@example.com', 'Google', 'New York', 2);

-- -- Insert into CoopAdvisor
-- INSERT INTO `CoopAdvisor` (`firstName`, `lastName`, `email`, `adminID`) VALUES
-- ('Sarah', 'James', 'sarah.james@northeastern.edu', 1),
-- ('Bruce', 'Taylor', 'bruce.taylor@northeastern.edu', 2);

-- -- Insert into Student
-- INSERT INTO `Student` (`firstName`, `lastName`, `email`, `company`, `city`, `adminID`, `advisorID`) VALUES
-- ('Tommy', 'Nelson', 'tommy.nelson@northeastern.edu', 'Draft Kings', 'New York', 1, 1),
-- ('Natasha', 'Smith', 'natasha.smith@northeastern.edu', 'Figma', 'Los Angeles', 2, 2);

-- -- Insert into Parent
-- INSERT INTO `Parent` (`relationshipToStudent`) VALUES
-- ('Father'),
-- ('Mother');

-- -- Insert into StudentParent
-- INSERT INTO `StudentParent` (`studentID`, `parentID`) VALUES
-- (1, 1),
-- (2, 2);

-- -- Insert into Performance
-- INSERT INTO `Performance` (`metricName`, `value`, `adminID`) VALUES
-- ('User Engagement', 85, 1),
-- ('System Uptime', 99, 2);

-- -- Insert into Update
-- INSERT INTO `Updates` (`updateName`, `updateDescription`, `adminID`) VALUES
-- ('System Upgrade', 'Upgraded to version 2.0', 1),
-- ('Database Optimization', 'Indexes added to critical tables', 2);

-- -- Insert into AlumAdvisor
-- INSERT INTO `AlumAdvisor` (`alumID`, `advisorID`) VALUES
-- (1, 1),
-- (2, 2);

-- -- Insert into AlumStudent
-- INSERT INTO `AlumStudent` (`nuID`, `alumID`) VALUES
-- (1, 1),
-- (2, 2);

-- -- Insert into Apartment
-- INSERT INTO `Apartment` (`alumID`, `beds`, `baths`, `rent`, `description`, `dateAvailableFrom`, `dateAvailableTo`, `street`, `city`, `state`, `country`) VALUES
-- (1, 2, 1, 2000, 'Cozy 2-bedroom apartment in a quiet neighborhood.', '2024-01-01', '2024-12-31', 123, 'Boston', 'MA', 'USA'),
-- (2, 3, 2, 3000, 'Spacious 3-bedroom apartment near downtown.', '2024-02-01', '2024-11-30', 456, 'New York', 'NY', 'USA');

-- -- Insert into Recommendation
-- INSERT INTO `Recommendation` (`alumID`, `establishment`, `category`, `location`, `priceRating`) VALUES
-- (1, 'The Coffee Bean', 'Cafe', 'Boston', 3),
-- (2, 'Joes Pizza', 'Restaurant', 'New York', 4);

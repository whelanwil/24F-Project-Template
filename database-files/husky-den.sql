DROP DATABASE IF EXISTS huskyDenDB;
CREATE DATABASE huskyDenDB;
USE huskyDenDB;

DROP TABLE IF EXISTS `SystemAdministrator`;
CREATE TABLE `SystemAdministrator` (
    `adminID` INTEGER AUTO_INCREMENT PRIMARY KEY ,
    `firstName` VARCHAR(50),
    `lastName` VARCHAR(50),
    `email` VARCHAR(75)
);

DROP TABLE IF EXISTS `Alumni`;
CREATE TABLE `Alumni` (
    `alumID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
    `advisorID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
    `nuID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
    `parentID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
    `metricID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
CREATE TABLE `Updates` (
    `updateID` INTEGER AUTO_INCREMENT PRIMARY KEY,
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
    `housingID` INTEGER AUTO_INCREMENT NOT NULL,
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
    PRIMARY KEY (`housingID`,`alumID`),
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni` (`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
DROP TABLE IF EXISTS `Recommendation`;
CREATE TABLE `Recommendation` (
    `alumID` INTEGER NOT NULL,
    `establishmentID` INTEGER AUTO_INCREMENT NOT NULL,
    `establishment` VARCHAR(75),
    `category` VARCHAR(75),
    `location` VARCHAR(75),
    `priceRating` INTEGER NOT NULL,
    PRIMARY KEY (`establishmentID`, `alumID`),
    FOREIGN KEY (`alumID`)
        REFERENCES `Alumni` (`alumID`)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

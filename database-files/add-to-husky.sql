USE huskyDenDB;

INSERT INTO `SystemAdministrator` (`adminID`, `firstName`, `lastName`, `email`) VALUES
(1, 'Jordan', 'Lee', 'jordan.lee@huskyden.com'),
(2, 'Bob', 'Johnson', 'bob.johnson@huskyden.com'),
(3, 'Alice', 'Smith', 'alice.smith@huskyden.com'),
(4, 'Michael', 'Brown', 'michael.brown@huskyden.com'),
(5, 'Emily', 'Davis', 'emily.davis@huskyden.com'),
(6, 'David', 'Wilson', 'david.wilson@huskyden.com'),
(7, 'Sophia', 'Moore', 'sophia.moore@huskyden.com'),
(8, 'James', 'Taylor', 'james.taylor@huskyden.com'),
(9, 'Olivia', 'Anderson', 'olivia.anderson@huskyden.com'),
(10, 'William', 'Thomas', 'william.thomas@huskyden.com'),
(11, 'Emma', 'Jackson', 'emma.jackson@huskyden.com'),
(12, 'Ethan', 'White', 'ethan.white@huskyden.com'),
(13, 'Isabella', 'Harris', 'isabella.harris@huskyden.com'),
(14, 'Benjamin', 'Martin', 'benjamin.martin@huskyden.com'),
(15, 'Mia', 'Thompson', 'mia.thompson@huskyden.com'),
(16, 'Logan', 'Garcia', 'logan.garcia@huskyden.com'),
(17, 'Ava', 'Martinez', 'ava.martinez@huskyden.com'),
(18, 'Lucas', 'Robinson', 'lucas.robinson@huskyden.com'),
(19, 'Charlotte', 'Clark', 'charlotte.clark@huskyden.com'),
(20, 'Mason', 'Rodriguez', 'mason.rodriguez@huskyden.com'),
(21, 'Amelia', 'Lewis', 'amelia.lewis@huskyden.com'),
(22, 'Alexander', 'Lee', 'alexander.lee@huskyden.com'),
(23, 'Harper', 'Walker', 'harper.walker@huskyden.com'),
(24, 'Henry', 'Hall', 'henry.hall@huskyden.com'),
(25, 'Ella', 'Allen', 'ella.allen@huskyden.com'),
(26, 'Michael', 'Young', 'michael.young@huskyden.com'),
(27, 'Lily', 'King', 'lily.king@huskyden.com'),
(28, 'Daniel', 'Wright', 'daniel.wright@huskyden.com'),
(29, 'Grace', 'Hill', 'grace.hill@huskyden.com'),
(30, 'Matthew', 'Scott', 'matthew.scott@huskyden.com'),
(31, 'Chloe', 'Green', 'chloe.green@huskyden.com'),
(32, 'Aiden', 'Adams', 'aiden.adams@huskyden.com'),
(33, 'Zoey', 'Baker', 'zoey.baker@huskyden.com'),
(34, 'Jackson', 'Nelson', 'jackson.nelson@huskyden.com'),
(35, 'Hannah', 'Carter', 'hannah.carter@huskyden.com'),
(36, 'Sebastian', 'Mitchell', 'sebastian.mitchell@huskyden.com'),
(37, 'Ella', 'Perez', 'ella.perez@huskyden.com'),
(38, 'Ryan', 'Roberts', 'ryan.roberts@huskyden.com'),
(39, 'Luna', 'Turner', 'luna.turner@huskyden.com'),
(40, 'Carter', 'Phillips', 'carter.phillips@huskyden.com');

INSERT INTO `Alumni` (`alumID`, `firstName`, `lastName`, `email`, `company`, `city`, `adminID`) VALUES
(1, 'Ashley', 'Schmidt', 'davidglover@payne.org', 'Moore, Little and Martinez', 'Rachelstad', 24),
(2, 'Antonio', 'Holt', 'margaret61@hotmail.com', 'Estrada, Robertson and Vaughn', 'Port Samantha', 34),
(3, 'Kurt', 'Reed', 'daniel49@marquez-thomas.biz', 'Robinson Inc', 'North Charleneville', 39),
(4, 'Zachary', 'Cox', 'dmelton@herrera.com', 'Haley-Collins', 'West Stevenshire', 19),
(5, 'Samuel', 'Wong', 'beckpaula@bowman.com', 'Beltran PLC', 'Williamborough', 23),
(6, 'Angela', 'McDonald', 'jprice@raymond.org', 'Walker-Ramos', 'Bradleytown', 18),
(7, 'Matthew', 'Hines', 'hannah41@hotmail.com', 'Lawrence-Rodgers', 'Smithside', 15),
(8, 'Sandra', 'Stone', 'terrymeyer@bennett.com', 'Johnson-Green', 'Port Savannah', 33),
(9, 'Laura', 'Hicks', 'crystalperez@hotmail.com', 'Garza, Johnson and Fowler', 'North Kimberlyland', 40),
(10, 'Jonathan', 'Dean', 'brandy62@yahoo.com', 'Jenkins, Johnson and Hayes', 'Lake Jennifer', 29),
(11, 'Melissa', 'Scott', 'rstrickland@heath.biz', 'Russell, Jackson and Walker', 'North Melissabury', 6),
(12, 'Tina', 'Howard', 'mendozalisa@graves.net', 'Adams LLC', 'East Alexisstad', 31),
(13, 'Jeffrey', 'Cole', 'julia56@gmail.com', 'Smith, Carter and Chavez', 'West Aaron', 8),
(14, 'Amanda', 'Hayes', 'benjamin76@gmail.com', 'Rodriguez, Flores and King', 'South Paulstad', 10),
(15, 'Thomas', 'Martinez', 'brownjeffrey@willis.info', 'Moore Inc', 'South Michaelton', 22),
(16, 'Brandon', 'Harper', 'melindabrown@gmail.com', 'Garcia, Mitchell and Barnes', 'Andrewchester', 11),
(17, 'Jessica', 'Fowler', 'williamphillips@coleman.com', 'Perez, Hughes and Harris', 'North David', 36),
(18, 'James', 'Morales', 'nicholas64@stevens.net', 'Martinez LLC', 'Gonzalezborough', 27),
(19, 'Andrew', 'Hunt', 'ashleycabrera@freeman.biz', 'Taylor-Robinson', 'Port Emily', 21),
(20, 'Lisa', 'Berry', 'victoriabowen@hotmail.com', 'White, Nguyen and Webb', 'North Kim', 7),
(21, 'Christine', 'Spencer', 'tina35@yahoo.com', 'Smith LLC', 'Port Jacobview', 4),
(22, 'Diana', 'Erickson', 'williamlewis@yahoo.com', 'Young and Sons', 'West Amy', 26),
(23, 'Megan', 'Rivera', 'garylopez@gmail.com', 'White and Sons', 'South Charles', 37),
(24, 'Stephen', 'Reyes', 'jamie68@yahoo.com', 'Rodriguez-Hall', 'North Tammyfort', 13),
(25, 'Karen', 'Williamson', 'michelledavis@yahoo.com', 'Adams and Sons', 'South Daniel', 20),
(26, 'Rebecca', 'Wells', 'johnsonadam@garcia.com', 'James-Wright', 'East Brian', 30),
(27, 'Benjamin', 'Ford', 'denisemontgomery@phillips.net', 'Young LLC', 'Port Melissa', 28),
(28, 'Edward', 'Greene', 'nicholasnguyen@lee.com', 'Jackson-Harris', 'East Sarahstad', 32),
(29, 'Julie', 'Alexander', 'kyle12@gmail.com', 'Nguyen-Williams', 'South Brianton', 25),
(30, 'Kimberly', 'Harvey', 'adamslisa@gmail.com', 'Fisher Inc', 'Lake Christina', 3),
(31, 'Lauren', 'Carroll', 'jamesallen@yahoo.com', 'Stewart-Hunt', 'West Courtney', 12),
(32, 'Rachel', 'Perez', 'sandralopez@hotmail.com', 'Hill-Baker', 'North Melanie', 17),
(33, 'Deborah', 'Dunn', 'thomas93@gmail.com', 'Howard-Sullivan', 'Port Lisa', 5),
(34, 'Nicholas', 'Hansen', 'bradleywatkins@gmail.com', 'Gomez LLC', 'North Stephen', 35),
(35, 'Steven', 'Vargas', 'floydsmith@freeman.net', 'Martinez, Gonzalez and Jenkins', 'Lake Patrick', 9),
(36, 'Patrick', 'Bryant', 'lisataylor@webb.org', 'Collins Inc', 'South Amy', 2),
(37, 'Donald', 'Armstrong', 'mark75@gmail.com', 'Young LLC', 'Lake Victoria', 1),
(38, 'Victoria', 'Matthews', 'andrew39@robinson.com', 'Smith-Carter', 'New Lauren', 14),
(39, 'Anthony', 'George', 'brandoncampbell@yahoo.com', 'Moore-Howard', 'West Andrewville', 38),
(40, 'Maria', 'Ellis', 'alexanderturner@gmail.com', 'King PLC', 'East Jessica', 23),
(41, 'Alexander', 'Freeman', 'danielmorgan@gmail.com', 'Hernandez PLC', 'New Tammymouth', 18),
(42, 'Stephanie', 'Curtis', 'michaeljames@yahoo.com', 'Anderson, Stewart and Ramos', 'Lake Shannon', 39),
(43, 'Catherine', 'Long', 'williamrussell@gmail.com', 'Smith, Foster and Lopez', 'North Bryan', 16),
(44, 'Gregory', 'Powell', 'edwardharrison@hotmail.com', 'Jones, Perry and Nguyen', 'New Maria', 6),
(45, 'Sharon', 'Flores', 'davidhart@yahoo.com', 'Williams-Walker', 'North Michael', 24),
(46, 'Aaron', 'Warren', 'kelly12@yahoo.com', 'Moore Ltd', 'South Christina', 8),
(47, 'Judy', 'Ross', 'paulallen@gmail.com', 'Garcia Group', 'New James', 40),
(48, 'Janet', 'Mills', 'kimberlywatson@gmail.com', 'Fisher-James', 'West Davidton', 10),
(49, 'Justin', 'Reed', 'aaronharris@hotmail.com', 'Morris, Lewis and Martin', 'Port Brandon', 19),
(50, 'Christina', 'Kim', 'brianna82@yahoo.com', 'Henderson and Sons', 'North Amanda', 34);

INSERT INTO `CoopAdvisor` (`advisorID`, `firstName`, `lastName`, `email`, `adminID`) VALUES
(1, 'Michael', 'Boyd', 'brianhall@brown.biz', 34),
(2, 'Michael', 'Reynolds', 'daltonjessica@martin.com', 40),
(3, 'Candace', 'Mcknight', 'lrussell@frazier.com', 16),
(4, 'Allen', 'Nicholson', 'christypeck@hotmail.com', 10),
(5, 'Jonathan', 'Woods', 'fisherelizabeth@wright-medina.biz', 30),
(6, 'Jessica', 'Craig', 'susan39@parsons.biz', 28),
(7, 'Rebecca', 'Glover', 'scottmark@hotmail.com', 13),
(8, 'Christopher', 'Henderson', 'mjackson@bailey.net', 18),
(9, 'Angela', 'Porter', 'erichernandez@yahoo.com', 24),
(10, 'Thomas', 'May', 'scotthart@hotmail.com', 7),
(11, 'Benjamin', 'Caldwell', 'ashley31@gmail.com', 9),
(12, 'Laura', 'Patton', 'karenscott@yahoo.com', 33),
(13, 'Brandon', 'Griffith', 'christian82@lynch.com', 21),
(14, 'Rachel', 'Jenkins', 'morris92@gmail.com', 26),
(15, 'Aaron', 'Bass', 'ericksonamy@gmail.com', 15),
(16, 'Michelle', 'Mathis', 'denisemiller@yahoo.com', 27),
(17, 'Steven', 'Johnston', 'jacobgomez@yahoo.com', 25),
(18, 'Deborah', 'Clayton', 'ryanmiller@gmail.com', 36),
(19, 'Edward', 'Cole', 'carpenterjohn@yahoo.com', 32),
(20, 'Elizabeth', 'Cummings', 'denisejackson@hotmail.com', 19),
(21, 'Megan', 'Harper', 'johnsondaniel@lopez.com', 11),
(22, 'Shawn', 'Frazier', 'rogermartin@yahoo.com', 31),
(23, 'Kelly', 'Walters', 'thomasallen@yahoo.com', 29),
(24, 'Andrew', 'Hoffman', 'brandonsimmons@gmail.com', 22),
(25, 'Justin', 'Moore', 'alexander86@hotmail.com', 1),
(26, 'Kathleen', 'Shaw', 'emilyturner@gmail.com', 6),
(27, 'Christine', 'Mann', 'vickie74@yahoo.com', 14),
(28, 'Patrick', 'Gardner', 'karenbennett@yahoo.com', 37),
(29, 'Lisa', 'Gonzalez', 'robert86@hotmail.com', 35),
(30, 'Timothy', 'Haynes', 'gonzalezbeth@gmail.com', 20),
(31, 'Hannah', 'Hawkins', 'ronaldmartinez@yahoo.com', 2),
(32, 'Victoria', 'Stevenson', 'laurabrown@hotmail.com', 3),
(33, 'Julie', 'Fox', 'amysmith@anderson.biz', 8),
(34, 'Henry', 'Frank', 'timothywood@hotmail.com', 5),
(35, 'Catherine', 'Bryan', 'kevin82@yahoo.com', 23),
(36, 'Sara', 'Barber', 'alexhill@gmail.com', 4),
(37, 'Tina', 'Watkins', 'craigmills@lynch.com', 38),
(38, 'Russell', 'Horton', 'holly83@hotmail.com', 17),
(39, 'Joshua', 'Curtis', 'joseph77@gmail.com', 12),
(40, 'Maria', 'Shields', 'michellenichols@yahoo.com', 16),
(41, 'Jennifer', 'Graves', 'lisarodriguez@gmail.com', 39),
(42, 'Anthony', 'Pierce', 'jessica63@yahoo.com', 34),
(43, 'Ryan', 'Perry', 'hutchinsoncheryl@gmail.com', 10),
(44, 'Danielle', 'Grant', 'kelly60@ford.biz', 28),
(45, 'Emily', 'Watson', 'davidjohnson@gmail.com', 18),
(46, 'Mark', 'Clark', 'rebeccaking@yahoo.com', 21),
(47, 'Heather', 'Crawford', 'cody75@gmail.com', 11),
(48, 'Diana', 'Ramsey', 'dannyhoward@gmail.com', 20),
(49, 'Brian', 'Watts', 'sara78@gmail.com', 24),
(50, 'Linda', 'Fletcher', 'james32@yahoo.com', 9);

INSERT INTO `Student` (`nuID`, `firstName`, `lastName`, `email`, `company`, `city`, `adminID`, `advisorID`) VALUES
(1, 'Joseph', 'Evans', 'julianadams@cummings-nunez.net', 'Kelly-Wheeler', 'Lake Kenneth', 5, 36),
(2, 'William', 'Wilson', 'xpeters@hotmail.com', 'Logan, Harrison and Cabrera', 'Howardburgh', 31, 17),
(3, 'Michael', 'Smith', 'emilybrown@hotmail.com', 'Collins Inc', 'West Elijahton', 5, 3),
(4, 'Carol', 'Harvey', 'zdavis@yahoo.com', 'Thompson Group', 'West Bruceborough', 36, 4),
(5, 'Laura', 'Johnson', 'amy79@mills-baker.info', 'Mcbride-White', 'Swansonburgh', 6, 46),
(6, 'Mark', 'Martin', 'anthony98@yahoo.com', 'Hernandez, Davis and Gill', 'New Johnmouth', 28, 41),
(7, 'Sandra', 'Phillips', 'garyharris@hansen-hughes.org', 'Brown-Williams', 'Samanthafort', 34, 33),
(8, 'Katherine', 'Harrison', 'susan83@hotmail.com', 'Cooper-Johnson', 'North Michaelfort', 40, 6),
(9, 'David', 'Howard', 'johngonzalez@gmail.com', 'Morgan PLC', 'South Cindyport', 24, 35),
(10, 'Brian', 'Gonzales', 'lisahernandez@gmail.com', 'Lewis and Sons', 'Williambury', 29, 10),
(11, 'Rebecca', 'White', 'kelly92@hotmail.com', 'Williams-Williams', 'Port Jamie', 4, 11),
(12, 'Lisa', 'Morris', 'mckenzieflores@hughes.com', 'Johnson Inc', 'Lake Amyville', 17, 14),
(13, 'Karen', 'Russell', 'josephmurphy@davis.biz', 'Nguyen PLC', 'Maryberg', 20, 15),
(14, 'Jonathan', 'Alexander', 'robinsonjack@gmail.com', 'Thompson-Kennedy', 'Jeffreyburgh', 21, 19),
(15, 'James', 'Foster', 'rachelharris@gmail.com', 'Edwards-Ramirez', 'South Susantown', 3, 48),
(16, 'Jessica', 'Brooks', 'scottallen@hotmail.com', 'Harris, Young and Ross', 'Brendafort', 18, 49),
(17, 'Paul', 'Kelly', 'kimberlyking@yahoo.com', 'Hill, Coleman and Roberts', 'Lake Laurafort', 27, 24),
(18, 'Emily', 'Campbell', 'jamesanderson@hotmail.com', 'Baker-Wood', 'South Matthewfort', 9, 8),
(19, 'Edward', 'Nelson', 'garyrobinson@gmail.com', 'Thomas-Gonzalez', 'Port Lisa', 38, 7),
(20, 'Karen', 'Allen', 'richardlewis@yahoo.com', 'Lopez-Moore', 'Lake Kathyland', 22, 29),
(21, 'Angela', 'Lopez', 'ronaldsimmons@gmail.com', 'Phillips-Johnson', 'North Nathanville', 19, 2),
(22, 'Michelle', 'Peterson', 'benjaminmartinez@hotmail.com', 'Murphy, Harris and Johnson', 'North Tylerland', 8, 16),
(23, 'Elizabeth', 'Torres', 'danielperry@gmail.com', 'Clark-Young', 'South Kaylatown', 14, 50),
(24, 'Victoria', 'Mitchell', 'davidsmith@gmail.com', 'Clark LLC', 'Port Josephville', 15, 28),
(25, 'Maria', 'Bailey', 'rachelmartinez@yahoo.com', 'Martinez-Campbell', 'Cynthiabury', 30, 34),
(26, 'Hannah', 'Ward', 'johnthomas@austin.com', 'Wood, Nelson and Alexander', 'South Matthewfort', 2, 18),
(27, 'Amy', 'Garcia', 'robertbrown@gmail.com', 'Nelson-Thomas', 'East Kimberlyport', 37, 25),
(28, 'Peter', 'Reed', 'nicholas99@hotmail.com', 'Moore-Jackson', 'Karenchester', 23, 31),
(29, 'Christopher', 'Perry', 'davidgonzalez@yahoo.com', 'Foster Group', 'South Jacobfort', 26, 12),
(30, 'Lauren', 'Stewart', 'michaelharrison@yahoo.com', 'Fowler-Hernandez', 'West Sharonville', 13, 20),
(31, 'Charles', 'Cruz', 'melissawalker@gmail.com', 'Gray, Kelly and King', 'North Jasonport', 12, 13),
(32, 'Steven', 'Baker', 'jasonmorris@hotmail.com', 'Thompson-Henderson', 'South Ericfort', 32, 40),
(33, 'Nancy', 'Roberts', 'michaelgonzalez@gmail.com', 'Martinez-Johnson', 'North Debbiechester', 16, 26),
(34, 'Ryan', 'Hill', 'matthewgonzalez@yahoo.com', 'Scott LLC', 'Lake Sherrybury', 36, 47),
(35, 'Ashley', 'Watson', 'cynthiarodriguez@gmail.com', 'Nelson-Jackson', 'Matthewtown', 1, 1),
(36, 'Patrick', 'Bryant', 'sarahjackson@gmail.com', 'Perez-Hill', 'New Brianberg', 6, 9),
(37, 'Heather', 'Harris', 'ericthomas@hotmail.com', 'Mitchell-Morris', 'North Christopherfort', 34, 4),
(38, 'Diana', 'Powell', 'rebeccajames@gmail.com', 'Perez Inc', 'South Paula', 28, 42),
(39, 'George', 'Henderson', 'brianmartinez@gmail.com', 'Ward and Sons', 'Johnville', 40, 45),
(40, 'Kevin', 'Sanchez', 'robinmartinez@hotmail.com', 'Williams, Gray and Taylor', 'Amyfort', 10, 30),
(41, 'Alice', 'Ross', 'amydavidson@gmail.com', 'Bailey-Garza', 'East Robertmouth', 5, 21),
(42, 'Nicholas', 'Bennett', 'karenlong@yahoo.com', 'Davis and Sons', 'West Nicoleview', 25, 37),
(43, 'Catherine', 'Gonzalez', 'johnsonjacob@hotmail.com', 'Robinson and Sons', 'New Michaelborough', 11, 44),
(44, 'Deborah', 'Cox', 'jacobjohnson@hotmail.com', 'Carter-Jones', 'Josephstad', 39, 38),
(45, 'Aaron', 'Mason', 'kelly32@gmail.com', 'Nelson-Ramirez', 'Lake Brandonburgh', 7, 5),
(46, 'Sandra', 'Carter', 'nicholasyoung@gmail.com', 'Johnson, Adams and Torres', 'Port Laura', 33, 27),
(47, 'Andrew', 'Long', 'kimberlyrogers@gmail.com', 'Adams-Harris', 'South Jeffreystad', 35, 43),
(48, 'Anna', 'Phillips', 'lisaparker@hotmail.com', 'Bailey, Perry and King', 'Lake Gregory', 3, 39),
(49, 'Jeremy', 'Campbell', 'ronaldking@yahoo.com', 'Davis-Williams', 'North Deborah', 13, 23),
(50, 'Sophia', 'Martinez', 'andreasmith@gmail.com', 'Walker-King', 'East Henryville', 22, 32);

INSERT INTO `Parent` (`parentID`, `relationshipToStudent`) VALUES
(1, 'Stepmother'),
(2, 'Grandparent'),
(3, 'Grandparent'),
(4, 'Stepmother'),
(5, 'Grandparent'),
(6, 'Father'),
(7, 'Mother'),
(8, 'Guardian'),
(9, 'Father'),
(10, 'Stepmother'),
(11, 'Mother'),
(12, 'Grandparent'),
(13, 'Mother'),
(14, 'Guardian'),
(15, 'Stepfather'),
(16, 'Stepmother'),
(17, 'Grandparent'),
(18, 'Guardian'),
(19, 'Father'),
(20, 'Stepfather'),
(21, 'Mother'),
(22, 'Stepmother'),
(23, 'Mother'),
(24, 'Father'),
(25, 'Stepfather'),
(26, 'Grandparent'),
(27, 'Mother'),
(28, 'Father'),
(29, 'Guardian'),
(30, 'Stepmother'),
(31, 'Mother'),
(32, 'Stepfather'),
(33, 'Father'),
(34, 'Grandparent'),
(35, 'Guardian'),
(36, 'Stepmother'),
(37, 'Father'),
(38, 'Stepfather'),
(39, 'Guardian'),
(40, 'Mother'),
(41, 'Grandparent'),
(42, 'Stepmother'),
(43, 'Stepfather'),
(44, 'Guardian'),
(45, 'Father'),
(46, 'Mother'),
(47, 'Grandparent'),
(48, 'Guardian'),
(49, 'Stepmother'),
(50, 'Father');

INSERT INTO `StudentParent` (`studentID`, `parentID`) VALUES
(15, 1),
(3, 11),
(49, 42),
(24, 30),
(8, 47),
(32, 28),
(18, 33),
(25, 8),
(5, 9),
(22, 14),
(46, 3),
(34, 12),
(41, 37),
(30, 15),
(45, 43),
(16, 19),
(11, 26),
(13, 5),
(31, 29),
(40, 20),
(6, 10),
(39, 6),
(21, 40),
(33, 41),
(28, 4),
(48, 2),
(17, 22),
(23, 16),
(10, 7),
(14, 18),
(20, 31),
(38, 21),
(42, 13),
(44, 27),
(9, 17),
(27, 35),
(29, 36),
(26, 24),
(4, 25),
(35, 23),
(2, 39),
(43, 34),
(1, 38),
(7, 32),
(12, 45),
(19, 44),
(47, 46),
(50, 48),
(36, 49);

INSERT INTO `Performance` (`metricID`, `metricName`, `value`, `adminID`) VALUES
(1, 'Extracurricular Participation', 99, 3),
(2, 'GPA', 88, 30),
(3, 'GPA', 88, 1),
(4, 'Extracurricular Participation', 64, 24),
(5, 'Extracurricular Participation', 79, 29),
(6, 'Attendance', 72, 15),
(7, 'GPA', 93, 28),
(8, 'Co-op Hours', 86, 12),
(9, 'Project Completion', 57, 7),
(10, 'Attendance', 85, 31),
(11, 'Co-op Hours', 77, 9),
(12, 'GPA', 60, 25),
(13, 'Project Completion', 89, 20),
(14, 'Attendance', 95, 34),
(15, 'Co-op Hours', 82, 11),
(16, 'Extracurricular Participation', 69, 16),
(17, 'Attendance', 90, 19),
(18, 'Co-op Hours', 74, 21),
(19, 'Attendance', 91, 32),
(20, 'Project Completion', 63, 40),
(21, 'Attendance', 70, 5),
(22, 'Extracurricular Participation', 84, 18),
(23, 'Project Completion', 93, 37),
(24, 'Attendance', 75, 14),
(25, 'Co-op Hours', 89, 27),
(26, 'GPA', 97, 35),
(27, 'Attendance', 83, 22),
(28, 'GPA', 68, 10),
(29, 'Extracurricular Participation', 73, 6),
(30, 'Attendance', 87, 4),
(31, 'Co-op Hours', 81, 2),
(32, 'Extracurricular Participation', 66, 8),
(33, 'Project Completion', 98, 26),
(34, 'Attendance', 88, 13),
(35, 'Co-op Hours', 79, 38),
(36, 'Attendance', 80, 23),
(37, 'Extracurricular Participation', 85, 39),
(38, 'Attendance', 92, 36),
(39, 'GPA', 75, 17),
(40, 'Project Completion', 96, 33),
(41, 'Co-op Hours', 82, 29),
(42, 'Extracurricular Participation', 71, 20),
(43, 'Attendance', 84, 30),
(44, 'GPA', 86, 24),
(45, 'Project Completion', 94, 12),
(46, 'Co-op Hours', 80, 1),
(47, 'Attendance', 89, 15),
(48, 'Extracurricular Participation', 74, 9),
(49, 'GPA', 78, 11),
(50, 'Co-op Hours', 76, 7);


INSERT INTO `Updates` (`updateID`, `updateName`, `updateDescription`, `adminID`) VALUES
(1, 'Speech art.', 'Life girl station. Voice place exist term.', 8),
(2, 'Power.', 'Environmental newspaper phone among someone industry.', 13),
(3, 'Prevent some order.', 'Next various close school sense.', 20),
(4, 'Become Congress.', 'Test rule member watch success crime. Adult bill teacher.', 6),
(5, 'Physical some.', 'New score draw policy form daughter year bit.', 16),
(6, 'Laugh area.', 'Wife raise lose range. Matter weight soon however.', 31),
(7, 'Character century.', 'Market know foot. Parent trade behavior medical.', 12),
(8, 'World special test.', 'Rate present step floor. Save establish like window.', 27),
(9, 'Project condition.', 'Another laugh reality. Son stand live computer.', 35),
(10, 'Move very region.', 'Decide wrong season happy. Truth environmental quite.', 14),
(11, 'Social season purpose.', 'Authority write later customer recent.', 18),
(12, 'Effort cultural ability.', 'Explain term itself staff view management.', 25),
(13, 'See major event.', 'Indeed natural crime. Reduce concern whole.', 22),
(14, 'Money various.', 'Key cultural indicate early believe.', 32),
(15, 'Art person paper.', 'Grow industry minute read positive.', 28),
(16, 'Economic last.', 'Tax player among. Allow simply resource.', 10),
(17, 'School senior.', 'Medical quite task value. Body better floor live.', 4),
(18, 'Choose within public.', 'Step available force. Camera knowledge want.', 26),
(19, 'Similar report.', 'Deep spend yourself collection toward.', 15),
(20, 'Officer member.', 'Clear exist share lead. Interest style product.', 1),
(21, 'Political citizen.', 'Matter growth issue wrong.', 19),
(22, 'Level man itself.', 'Mission successful clearly. Truth case politics.', 34),
(23, 'Specific memory.', 'Decision security bill nature cultural.', 24),
(24, 'Picture key.', 'Person reality ready story.', 17),
(25, 'Half necessary.', 'Deep other education trial mention.', 30),
(26, 'Paper specific.', 'Eye politics create force. Political weight often.', 33),
(27, 'Stop station learn.', 'Place heart meet effect physical.', 37),
(28, 'Natural yourself.', 'Mother social individual explain government.', 7),
(29, 'Success continue.', 'Appear over want away reason. Play red everything.', 9),
(30, 'Every against.', 'Offer watch main understand trial.', 11);


INSERT INTO `Apartment` (`alumID`, `housingID`, `beds`, `baths`, `rent`, `description`, `dateAvailableFrom`, `dateAvailableTo`, `street`, `city`, `state`, `country`) VALUES
(1, 1, 4, 2, 2310, 'Modern apartment with tech-friendly amenities, ideal for engineers or tech alumni.', '2024-12-07 11:37:30', '2024-07-28 15:31:59', 6919, 'Lake Sue', 'West Virginia', 'USA'),
(2, 2, 1, 3, 2386, 'Fully furnished apartment, available for hard-working professionals or engineers.', '2024-12-18 23:52:03', '2024-10-23 22:00:45', 8688, 'Jamesburgh', 'New York', 'USA'),
(3, 3, 3, 2, 1643, 'Fully furnished apartment, available for hard-working professionals or engineers.', '2024-12-17 02:33:13', '2024-04-15 15:35:18', 2960, 'South Markmouth', 'Wisconsin', 'USA'),
(4, 4, 3, 1, 1506, 'Fully furnished apartment, available for hard-working professionals or engineers.', '2024-12-26 20:28:12', '2024-07-21 02:23:48', 3208, 'South Lisaland', 'Utah', 'USA'),
(5, 5, 3, 3, 2412, 'Family-friendly apartment with spacious interiors, great for alumni with children.', '2024-12-16 13:06:56', '2024-01-08 14:34:31', 3725, 'Kelseybury', 'West Virginia', 'USA'),
(6, 6, 4, 3, 2189, 'Cozy and modern apartment available, perfect for professionals or small families.', '2024-12-27 05:14:18', '2024-02-21 19:09:25', 2543, 'Davidton', 'Ohio', 'USA'),
(7, 7, 2, 2, 1444, 'Recently renovated unit, close to public transport, designed for comfortable living.', '2024-12-21 20:51:27', '2024-11-10 00:47:31', 6792, 'Samanthamouth', 'California', 'USA'),
(8, 8, 4, 2, 2218, 'Stylish unit with amenities; perfect for alumni starting their career journey.', '2024-12-06 01:21:36', '2024-05-26 15:31:51', 4977, 'Hubbardbury', 'Connecticut', 'USA'),
(9, 9, 3, 1, 2064, 'Apartment with great views, perfect for graduates looking for a peaceful environment.', '2024-12-15 20:44:50', '2024-02-05 07:57:04', 3104, 'West Jasonstad', 'Oregon', 'USA'),
(10, 10, 1, 1, 1507, 'Perfect apartment for alumni who graduated in 2014, seeking a work-life balance.', '2024-12-14 11:39:10', '2024-04-03 12:29:52', 6928, 'South Stephanieville', 'Kansas', 'USA'),
(11, 11, 2, 1, 1124, 'Modern apartment with tech-friendly amenities, ideal for engineers or tech alumni.', '2024-12-04 07:31:47', '2024-06-01 16:24:22', 1916, 'Port Kayla', 'Montana', 'USA'),
(12, 12, 3, 3, 2883, 'Bright and airy apartment located near key business districts, suitable for young alumni.', '2024-12-01 01:35:28', '2024-05-13 00:38:23', 4325, 'New Heatherport', 'Illinois', 'USA'),
(13, 13, 2, 2, 2408, 'Fully furnished apartment, available for hard-working professionals or engineers.', '2024-12-13 19:23:19', '2024-08-14 01:29:35', 5643, 'East Tinachester', 'Georgia', 'USA'),
(14, 14, 4, 2, 1849, 'Recently renovated unit, close to public transport, designed for comfortable living.', '2024-12-22 10:23:19', '2024-03-15 14:10:05', 4331, 'East Dawn', 'Texas', 'USA'),
(15, 15, 1, 1, 1248, 'Family-friendly apartment with spacious interiors, great for alumni with children.', '2024-12-20 09:30:11', '2024-10-22 11:01:45', 3156, 'South Jeff', 'Nevada', 'USA'),
(16, 16, 4, 3, 1577, 'Bright and airy apartment located near key business districts, suitable for young alumni.', '2024-12-18 14:41:24', '2024-09-06 18:51:22', 2749, 'Port Jamesland', 'Wyoming', 'USA'),
(17, 17, 3, 1, 1076, 'Apartment with great views, perfect for graduates looking for a peaceful environment.', '2024-12-28 12:49:55', '2024-08-30 20:19:12', 3482, 'Lake Katherine', 'Vermont', 'USA'),
(18, 18, 2, 1, 2831, 'Stylish unit with amenities; perfect for alumni starting their career journey.', '2024-12-19 09:54:03', '2024-04-02 02:44:18', 6587, 'West Jenniferville', 'Indiana', 'USA'),
(19, 19, 1, 1, 2327, 'Cozy and modern apartment available, perfect for professionals or small families.', '2024-12-07 13:01:30', '2024-02-19 16:42:17', 6890, 'North Amanda', 'Maine', 'USA'),
(20, 20, 2, 3, 1296, 'Family-friendly apartment with spacious interiors, great for alumni with children.', '2024-12-03 11:29:37', '2024-03-04 07:47:08', 7546, 'East Benjamin', 'Washington', 'USA'),
(21, 21, 4, 2, 1947, 'Apartment with great views, perfect for graduates looking for a peaceful environment.', '2024-12-29 22:50:04', '2024-06-21 10:30:31', 1112, 'Port Andrew', 'Colorado', 'USA'),
(22, 22, 3, 2, 2138, 'Stylish unit with amenities; perfect for alumni starting their career journey.', '2024-12-06 20:55:30', '2024-05-11 04:47:13', 1776, 'South Victorborough', 'Delaware', 'USA'),
(23, 23, 4, 3, 1258, 'Perfect apartment for alumni who graduated in 2014, seeking a work-life balance.', '2024-12-11 18:17:35', '2024-08-19 13:03:17', 3915, 'New Samuelchester', 'South Dakota', 'USA'),
(24, 24, 2, 2, 1057, 'Recently renovated unit, close to public transport, designed for comfortable living.', '2024-12-16 10:50:14', '2024-11-12 08:18:02', 8123, 'South Willieshire', 'North Dakota', 'USA'),
(25, 25, 1, 2, 1650, 'Cozy and modern apartment available, perfect for professionals or small families.', '2024-12-17 08:55:45', '2024-07-27 03:33:55', 4555, 'Lake Crystalview', 'Alabama', 'USA'),
(26, 26, 3, 2, 2733, 'Stylish unit with amenities; perfect for alumni starting their career journey.', '2024-12-09 23:35:10', '2024-02-11 19:07:46', 5261, 'South Caitlynstad', 'Nebraska', 'USA'),

INSERT INTO `Recommendation` (`alumID`, `establishment`, `category`, `location`, `priceRating`) VALUES
(1, 'Moore and Sons', 'Park', 'North Jose', 2),
(2, 'Roth-Henderson', 'Shopping Mall', 'Williamsport', 1),
(2, 'Frank, Robinson and Brown', 'Library', 'Tinabury', 5),
(4, 'Castillo-Lewis', 'Restaurant', 'Allisonmouth', 5),
(5, 'Jones Inc', 'Library', 'Jacksonside', 1),
(6, 'Walker-Morris', 'Cafe', 'South Jasonborough', 3),
(7, 'Martinez and Sons', 'Gym', 'Davidtown', 4),
(8, 'Brown-Moore', 'Park', 'West Kennethstad', 3),
(9, 'Adams-Williams', 'Shopping Mall', 'Lake Elizabeth', 5),
(10, 'Anderson and Associates', 'Library', 'Codytown', 2),
(11, 'Harris Ltd', 'Cafe', 'South Melissahaven', 4),
(12, 'Clark-Smith', 'Restaurant', 'Lake Nancyborough', 5),
(13, 'Smith-Wilson', 'Gym', 'Jenniferbury', 3),
(14, 'Thompson-Gomez', 'Park', 'New Craigchester', 1),
(15, 'Garcia LLC', 'Shopping Mall', 'North Ronald', 2),
(16, 'King-Robinson', 'Library', 'West Brianport', 3),
(17, 'Campbell Group', 'Cafe', 'Port Jeffrey', 4),
(18, 'Rodriguez, Foster and Brown', 'Restaurant', 'North Peter', 5),
(19, 'Perez Inc', 'Gym', 'East Michelle', 1),
(20, 'Phillips-Jackson', 'Park', 'New Jenniferton', 4),
(21, 'White, Hughes and Hernandez', 'Shopping Mall', 'Hannahview', 3),
(22, 'Gonzalez Ltd', 'Library', 'Sarahborough', 2),
(23, 'Evans-Ross', 'Cafe', 'South Charlesview', 5),
(24, 'Wilson-Adams', 'Restaurant', 'Port Kimberlyland', 4),
(25, 'Wood, Gray and Edwards', 'Gym', 'South Kristinstad', 2),
(26, 'Nelson and Sons', 'Park', 'South Paulchester', 3),
(27, 'Baker LLC', 'Shopping Mall', 'West Sydney', 4),
(28, 'Johnson-Johnson', 'Library', 'New Laura', 5),
(29, 'Carter Inc', 'Cafe', 'East Michaelton', 3),
(30, 'Lopez Group', 'Restaurant', 'Lake Benjamin', 1),
(31, 'Hernandez-Campbell', 'Gym', 'East Nicole', 2),
(32, 'Diaz Ltd', 'Park', 'South Kevin', 4),
(33, 'Powell-Price', 'Shopping Mall', 'Port Gabriellaberg', 3),
(34, 'Parker LLC', 'Library', 'Lake Michelemouth', 5),
(35, 'Brooks-Collins', 'Cafe', 'New Katie', 4),
(36, 'Kelly-James', 'Restaurant', 'North Markfort', 2),
(37, 'Sanders LLC', 'Gym', 'Port Sarahville', 3),
(38, 'Morris-Cruz', 'Park', 'East Tammyville', 4),
(39, 'Mitchell-Watson', 'Shopping Mall', 'West Lauraborough', 5),
(40, 'Reed LLC', 'Library', 'New Donaldstad', 2);
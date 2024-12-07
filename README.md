# Husky Den

# Our project
Husky Den is an app that connects Northeastern University students seeking co-op opportunities outside the Boston area with the university’s alumni network, providing housing support and fostering experiential learning by creating a smoother transition to new cities and broadening their real-world experiences. The vicious job market and limited Boston co-op options has pushed students to look across the country and abroad for opportunities more than ever before, however one major part of this step is finding your housing for this short period of time you're away from class. In the past, students have relied on friends, family, or sifted through countless online listings to find housing. However, Northeastern’s extensive alumni network, spanning across the globe, remains an untapped resource. By leveraging this network of individuals who understand the unique value of the co-op experience, the app connects students pursuing co-ops in various cities with alumni offering housing. Husky Den not only alleviates the stress of the co-op search but also encourages experiential learning and strengthens the bond between the university and its alumni.

Husky Den is a resource for students seeking co-op opportunities and alumni with extra space or sublets. It gives parents concerned about their child’s safety far from campus peace of mind, and offers a solution for co-op advisors frequently faced with logistical questions about global co-ops., With features including a map view and search tool to help students understand their commute, filters by city, major, degree, and distance to find the best housing fit, and secured but surfaced contact information to streamline the search to connect process, Husky Den is the comprehensive solution to Northeastern’s co-op housing challenges.

# Our team
Ashli Lao, Grace Uecker, Justin Haime, Salma Elmosallamy, & Grace Uecker

## How to build the containers
Before running the containers, you need to create the following secret files in the `secrets/` directory:

1. `mongodb_root_password.txt`
   - Contains the root password for MongoDB
   - Example: `MySecureRootPass123!`
   - This should be a strong password (12+ characters, mix of letters, numbers, symbols)

2. `mongodb_password.txt`
   - Contains the regular MongoDB user password
   - Example: `MySecureUserPass123!`
   - This is the password used by the application to connect to MongoDB

3. `jwt_secret.txt`
   - Contains the secret key used to sign JWT tokens
   - Example: `my-super-secret-key-for-jwt-tokens-2024`
   - Should be a long, random string (32+ characters recommended)

Important:
- Each file should contain only the password/secret (no newlines or extra spaces)
- These files are git-ignored and should never be committed to version control
- Keep these passwords secure and different from each other

# Video demo
https://drive.google.com/file/d/1LTnhDYwp758nLVbE1N0_nczr54yzUh8-/view?usp=sharing
You may need to refresh the page (you don't have to download it)
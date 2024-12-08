# Secure Session Management System

This project focuses on Secure Session Management while implementing an e-commerce website with features like product browsing, cart management, and checkout. To provide a safe and easy buying experience, it exhibits strong session handling, user authentication, and authorization procedures.

## Features
- Secure user authentication with role-based access control.
- Unique session management.
- Product browsing, cart management, and checkout functionality.
- Restriction of unauthorized access to sensitive operations.
- Testing for architectural breakers.
- Role-based access control with three types of users:
  - Authorized user: Can perform the task.
  - Unauthorized user: Cannot perform the task.
  - Unauthenticated user: Cannot access restricted areas.
 
## Architecture Breakers
- Predictable Session IDs: In order to take control of user sessions, attackers may be able to estimate session IDs. To avoid this, a unique session ID is generated for every user authentication.

- Mismanagement of Session Timeouts: Sessions may run too long or end too soon, risking usability and security. Having long session timeout period can allow attackers to hijack a session easily.

- Weak Encryption: There is a security concern because sensitive session data, like cart contents, are saved in plaintext. Session data is not currently encrypted, making it susceptible to possible leaks.

- Inadequate Authorization: Unauthorized users may gain access to tasks or checkout areas, which could be dangerous for security. To guarantee that only authorized users are given access, role-based access control is put into place.


## Test Cases
The application includes a robust testing suite to validate key aspects of the implementation, focusing on architecture breakers.

1. **Testing Database Existence**

Test Name: test_database_file_exists

This test verifies that the ecommerce.db SQLite database file is successfully generated during initialization. Even though it has nothing to do with an architectural breaker, the application may become unusable if the database is missing. The existence of the database is an essential requirement for the smooth functioning of the program.

2. **Testing Flask Application Activity**

Test Name: test_flask_project_running

This test confirms that the Flask application is set up successfully and can handle simple requests like the root and route. This guarantees the fundamental functionality of the application, even when it has nothing to do with an architectural breaker. The application may not be able to serve requests if Flask setup is incorrect.

3. **Testing Authentication Enforcement**

Test Name: test_authentication_required

This test makes sure that protected routes enforce authentication. Failure to enforce authentication can result in unauthorized access, violating security principles.  The current test case correctly handles authentication enforcement, ensuring security. This is one of the architectural breaker.

4. **Testing Unique Session ID**

Test Name: test_unique_session_id

This test confirms that each user login generates a unique session ID and that previous session IDs are invalidated when a user logs out. The confidentiality and integrity of session management could be affected by session fixation attacks resulting from a lack of unique session IDs. This architectural breaker is successfully avoided by the program by utilizing uuid.uuid4() to generate unique session IDs.

5. **Testing Session Timeout**

Test Name: test_session_timeout

This test determines if user sessions end after the timeout duration that has been set. Sessions can continue forever without session timeouts, which raises the possibility of unwanted access. Since the application's session length is set to 30 minutes, this test intentionally fails, which could be an architectural breaker. Setting up suitable timeouts reduces vulnerability to attacks.

6. **Testing Data Encryption**

Test Name: test_data_encryption

This test confirms that sensitive data, including session and product information, is stored securely (e.g., using encryption). Data security and confidentiality are violated if sensitive information is kept in plaintext, which allows attackers with database access to extract private information. The lack of encryption implementation in the program is one of the architectural breaker, which is why this test fails.


## Prerequisites
- **Python 3.7 or higher**  
- **pip** (Python package manager)  


## Steps to run the code

### Step 1: Create Databse directory
After cloning the project, create a new directory:
```bash
mkdir database
```

### Step 2: Change Directory
Navigate to the folder containing the project:
```bash
cd src
```

### Step 3: Run the Application
Execute the following command:

```bash
python -m app
```
The application will start running at http://127.0.0.1:5000/

### Step 4: Test the Application
Run the test suite using:
```bash
python test.py
```

## What the code does
This code uses the Flask framework to construct a secure session management system. Key capabilities like session monitoring, user authentication, authorization, and fundamental e-commerce-type functionalities are all included.

Users enter their login information. The system creates a session after verifying their login credentials. Users are given unique session identities when they log in, and these are maintained throughout their app activities. Role-based access control is enforced by the system, which grants or denies tasks access according to user roles. Product browsing, cart addition, content modification, and checkout (if authorized) are all available to users.

- **Login**: 
  Navigate to /login. Use the following credentials:
  - Authorized User:
    Username: authorized_user
    Password: password123
  - Unauthorized User:
    Username: unauthorized_user
    Password: password123

- **Products Page**: 
After logging in, visit /products to view and add products to your cart.

- **Cart Management**:
Access the cart at /cart to modify quantities or remove items.

- **Checkout**:
Authorized users can checkout at /checkout. Unauthorized users will receive an error message.

- **Task Handling**:
Only authorized users can perform tasks at /task.

- **Logout**:
Logout by visiting /logout.

## Frameworks and Libraries Used
- **Flask**: Web framework for routing and application logic.
- **SQLite**: Embedded database for storing product data.
- **uuid**: Used to generate unique session identifiers.
- **Unittest**: Framework for writing and running tests.

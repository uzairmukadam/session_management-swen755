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

## Implementation Overview

**app.py:** 
This mainly contains all the application logic. Define routes for authentication, products, shopping cart, and checkout. It has a strong system of session controls with session IDs which can be modified for timeouts. Control of authentication is done using decorators.

**db.py:** 
The file contains everything based on database management. Creates an SQLite database that allows for product data to be kept within.

**test.py:** 
This is solely the testing framework. Contains test scripts that purpose is to ensure session control is enabled and the application is securely working.



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

The code here uses the Flask framework to build a secure session management system. Key features of the code include session tracking, user authentication and authorization, and basic e-commerce type capabilities.

The user logs in to the app with his username and password. Upon validating the login credentials, the system creates a session for the user. In addition, unique session identities for users are created when users log in, which persist over their application activities. Tasks are granted or rejected, based on user roles enforced by the system. View the product, add items in the cart, modify the content, and checkout if authorized by the user.

- **Login**: 
  Access /login. Use the following credentials:
  - Authorized User:
    Username: authorized_user
    Password: password123
  - Unauthorized User:
    Username: unauthorized_user
    Password: password123

- **Products Page**: 
After logging in, visit /products to view and add products to your cart.

- **Cart Management**:
The cart is accessible at /cart, where quantities can be changed or items can be removed.

- **Checkout**:
Authorized users can checkout at /checkout. Unauthorized users are shown an error message.

- **Task Handling**:
Tasks at /task can only be carried out by an authorized user.

- **Logout**:
Log out using /logout.

## Frameworks and Libraries Used
- **Flask**: Web framework for routing and application logic.
- **SQLite**: Embedded database for storing product data.
- **uuid**: Used to generate unique session identifiers.
- **Unittest**: Framework for writing and running tests.

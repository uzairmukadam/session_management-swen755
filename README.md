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

- Session ID Uniqueness:
This test aims to avoid session reuse or hijacking by making sure that every user login creates a fresh, distinct session ID. In order to validate that the session IDs provided to each session are distinct, the test scenario requires logging in twice using the same credentials. It is expected that every login would generate a distinct session ID, guaranteeing strong session management and security.

- Session Timeout:
This test's objective is to confirm that sessions end appropriately after the specified timeout interval. Here, the user logs in and watches for the session to end. The user tries to access a protected route after the timeout has ended. In order to ensure secure session management, it is expected that the system will identify the expired session and reroute the user to the login page.


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

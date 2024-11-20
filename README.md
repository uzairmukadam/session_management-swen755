# Secure Session Management System

This project shows how to implement the "Secure Session Management" approach, which includes web application authorization, session handling, and authentication. The database is **SQLite**, and the system is constructed with **Flask**, a lightweight Python web framework.

### Features
- Authentication of users with unique session identifiers.
- Authorization checks for user operations.
- Persistent session management for tracking user actions.
- Simple e-commerce functionalities like viewing products, adding to a cart, and performing a task.
- Role-based access control with three types of users:
  - Authorized user: Can perform the task.
  - Unauthorized user: Cannot perform the task.
  - Unauthenticated user: Cannot access restricted areas.


## Prerequisites
- **Python 3.7 or higher**  
- **pip** (Python package manager)  


## Steps to run the code

### Step 1: Change Directory
Navigate to the folder containing the project:
```bash
cd sec
```

### Step 2: Run the Application
Execute the following command:

```bash
python -m app
```
The application will start running at http://127.0.0.1:5000/

## What the code does
This code implements a secure session management system using the Flask framework. It includes key features like user authentication, authorization, session tracking, and basic e-commerce-like functionality. 

Authentication- Users log in with their credentials. The system validates their username and password and establishes a session.
Session Management- Unique session identifiers are assigned to users upon logging in, which persist across their interactions with the app.
Authorization- The system enforces role-based access control, granting or denying access to tasks based on user roles.
Functionality- Users can browse products, add them to a cart, modify cart contents, and proceed to checkout (if authorized).

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

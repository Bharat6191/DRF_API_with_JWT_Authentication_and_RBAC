# DRF_API_with_JWT_Authentication_and_RBAC
This project is a RESTful API built using Django Rest Framework (DRF) that implements user authentication with JWT (JSON Web Token) and Role-Based Access Control (RBAC). The API allows user registration, login, and role-based access to CRUD operations on a sample resource, "projects." 

# DRF_API_with_JWT_Authentication_and_RBAC

1. User Registration and Authentication:
  * Secure password hashing
  * JWT-based token authentication for secure communication.

2. Role-Based Access Control (RBAC):
  * Two user roles: admin and user.
  * Admin can create, update, delete, and view resources.
  * User can only view resources.
3. CRUD Operations:
  * RESTful API endpoints for managing "projects."


# Requirements

  * Python 3.8+
  * Django 5.1+
  * Django Rest Framework (DRF)
  * rest_framework_simplejwt
  * A virtual environment (e.g., authenv)

# Setup and Installation Guide

1. Clone the Repository

''' 
  git clone <repository_url>
  cd <repository_name>

2. Set Up a Virtual Environment
Create and activate a virtual environment:

'''
  python3 -m venv authenv
  source authenv/bin/activate

3. Install Dependencies
Install the required Python packages:

'''
  pip install -r requirements.txt

4. Create and Configure the Database
Run migrations to set up the database:

'''
  python manage.py makemigrations
  python manage.py migrate

5. Create a Superuser
Create an admin user to access the Django Admin interface:
'''
  python manage.py createsuperuser


6. Run the Server
Start the Django development server:

'''
python manage.py runserver

The server will be available at http://127.0.0.1:8000/.

# API Endpoints

## User Authentication
  * Register User
  * POST /account/register/
  * Body:
    ''' 
        {
        "username": "example",
        "password": "password123",
        "role": "user"
        }
  * Response:
    
      {
        "message": "User registered successfully."
      }



## User Login
  * Login User
  * POST /account/login/
  * Body:
    ''' 
        {
          "username": "example",
          "password": "password123"
        }
  * Response:
    
      {
        "access_token": "JWT_TOKEN"
      }


## User Logout
  * Logout User
  * POST /account/logout/
  * Body:
    ''' 
        {
          "refresh_token": "REFRESH_TOKEN"
        }
  * Response:
    
      {
        "message": "Successfully logged out."
      }
# CRUD Operations on "Projects"
  ##  View Projects (Accessible to all users)
  * GET /account/projects/
  * Body:
    ''' 
        {
  "projects": [
      {
      "id": 1,
      "project_name": "Project A",
      "created_by": "admin",
      "created_at": "2024-12-01T12:00:00Z"
    }
  ]
}

##  Create Project (Admin only)
  * POST /account/projects/create/
  * Body:
    {
    "project_name": "Project B"
    }
  * Response:
    {
    "message": "Project created successfully."
    }









# Author
Bharat Solanke
https://www.linkedin.com/in/bharat-solanke-175286249/

___


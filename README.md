# DRF_API_with_JWT_Authentication_and_RBAC
This project is a RESTful API built using Django Rest Framework (DRF) that implements user authentication with JWT (JSON Web Token) and Role-Based Access Control (RBAC). The API allows user registration, login, and role-based access to CRUD operations on a sample resource, "projects."

## Features

### 1. User Registration and Authentication:
  * Secure password hashing
  * JWT-based token authentication for secure communication.

### 2. Role-Based Access Control (RBAC):
  * Two user roles: admin and user.
  * Admin can create, update, delete, and view resources.
  * User can only view resources.

### 3. CRUD Operations:
  * RESTful API endpoints for managing "projects."

## Requirements
  * Python 3.8+
  * Django 5.1+
  * Django Rest Framework (DRF)
  * `rest_framework_simplejwt`
  * A virtual environment (e.g., authenv)

## Setup and Installation Guide

### 1. Clone the Repository
Clone the repository to your local machine:

``` bash
git clone <repository_url>
cd <repository_name>


### 2. Set Up a Virtual Environment
Create and activate a virtual environment:

'''bash
  python3 -m venv authenv
  source authenv/bin/activate

3. Install Dependencies
Install the required Python packages:

'''bash
  pip install -r requirements.txt

4. Create and Configure the Database
Run migrations to set up the database:

'''bash
  python manage.py makemigrations
  python manage.py migrate

5. Create a Superuser
Create an admin user to access the Django Admin interface:
'''bash
  python manage.py createsuperuser


6. Run the Server
Start the Django development server:

'''bash
python manage.py runserver

The server will be available at http://127.0.0.1:8000/.

# API Endpoints

## User Authentication
  * Register User
  * POST /account/register/
  * Body:
    ''' bash
        {
        "username": "example",
        "password": "password123",
        "role": "user"
        }
  * Response:
    ```bash
      {
        "message": "User registered successfully."
      }
    



# Author
Bharat Solanke
https://www.linkedin.com/in/bharat-solanke-175286249/

___


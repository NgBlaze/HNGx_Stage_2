## UML IMAGE

![UML Image](https://github.com/NgBlaze/HNGx_Stage_2/blob/main/CRUD.drawio.png)

# API Documentation

This document provides an overview of the REST API endpoints, standard request and response formats, sample usage, known limitations, and instructions for setting up and deploying the API.

## Endpoints

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

### 1. Create a Person

**Endpoint:** '/api/'
**Method:** POST
**Request Format:**

{
"id": 1,
"name": "John Doe",
"age": 30
}

### 2. Retrieve a Person

**Endpoint:** '/api/<int:pk>'
**Method:** GET
**Request Format:**
{
"id": 1,
"name": "John Doe",
"age": 30
}

### 3. Update a Person

**Endpoint:** '/api/<int:pk>'
**Method:** PUT or PATCH
**Request Format:**
{
"name": "Updated Name",
"age": 35
}
**Response Format:**
{
"id": 1,
"name": "Updated Name",
"age": 35
}

### 4. Delete a Person

**Endpoint:** '/api/<int:pk>'
**Method:** DELETE
**Response Format:** No content (204 No Content)

### 4. Dynamic Parameter Handling

**Endpoint:** '/api/<str:name>'
**Method:** GET (Retrieve), PUT or PATCH (Update), DELETE (Delete)
**Response Format:**
{
"id": 1,
"name": "John Doe",
"age": 30
}

## Sample Usage

### Create a Person

**Request:**
POST https://ngblaze.pythonanywhere.com/api/
Content-Type: application/json

{
"name": "Alice Johnson",
"age": 25
}
**Response:**
{
"id": 2,
"name": "Alice Johnson",
"age": 25
}

### Retrieve a Person

**Request:**
GET https://ngblaze.pythonanywhere.com/api/2/
**Response:**
{
"id": 2,
"name": "Alice Johnson",
"age": 25
}

### Update a Person

**Request:**
PUT https://ngblaze.pythonanywhere.com/api/2/
Content-Type: application/json

{
"name": "Updated Name",
"age": 30
}
**Response:**
{
"id": 2,
"name": "Updated Name",
"age": 30
}

### Delete a Person

**Request:**
DELETE https://ngblaze.pythonanywhere.com/api/2/
**Response:** No content (204 No Content)

### Dynamic Parameter Handling

**Retrieve a Person by Name**

**Request:**
GET https://ngblaze.pythonanywhere.com/api/John%20Doe/
**Response:**
{
"id": 1,
"name": "John Doe",
"age": 30
}

## Known Limitations and Assumptions

- The API assumes that the `name` field for a person is unique.
- No authentication or authorization mechanisms are implemented in this example API. Consider adding authentication and authorization for production use.
- Error handling and validation of request data have been simplified for this example and should be enhanced for a production-ready API.

## Setup and Deployment Instructions

1.  Clone this repository: `git clone https://github.com/yourusername/your-api.git`
2.  Navigate to the project directory: `cd your-api`
3.  Create a virtual environment: `python -m venv venv`
4.  Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS and Linux: `source venv/bin/activate`
5.  Install project dependencies: `pip install -r requirements.txt`
6.  Apply database migrations: `python manage.py migrate`
7.  Start the development server: `python manage.py runserver`

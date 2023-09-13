![UML Image](https://github.com/NgBlaze/HNGx_Stage_2/blob/main/CRUD.drawio.png)

# API Documentation

This document provides an overview of the REST API endpoints, standard request and response formats, sample usage, known limitations, and instructions for setting up and deploying the API.

## Endpoints



## Create a User (POST)

**Endpoint:** '/api/'
**Method:** POST
**Request Format:** 

```json POST /api/ 

**Response (Status 201 Created):**
{
    "id": 1,
    "name": "precious"
}

**

## Retrieve a User by Name (GET)**

**

Endpoint: `/api/?name={person_name}`

**Request:**

GET /api/?name=precious

**Response (Status 200 OK):**
[
    {
        "id": 1,
        "name": "precious"
    }
]

## Update a User (PUT/PATCH)

Endpoint: `/api/{person_name}/`

**Request:**
PUT /api/precious/
{
    "name": "Updated Name"
}

**Response (Status 200 OK):**
{
    "id": 1,
    "name": "Updated Name"
}

## Delete a User (DELETE)

Endpoint: `/api/{person_name}/`

**Request:**
DELETE /api/precious/

**Response (Status 204 No Content):** 
No content returned.

## **Limitations and Assumptions**

-   This API assumes that each person's name is unique.
-   Only the "name" attribute is supported for CRUD operations.
-   Error handling and validation may need improvement for production use.

## **Setup and Deployment**

Follow these steps to set up and deploy the API:
**Clone this repository:**
git clone https://github.com/NgBlaze/HNGx_Stage_2

**Navigate to the project directory:**
cd django-rest-api

**Create a virtual environment and activate it:**
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

**Install project dependencies:**
pip install -r requirements.txt

**Apply database migrations:**
python manage.py migrate

**Start the development server**
python manage.py runserver




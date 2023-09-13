# Django REST API Documentation

## Overview

This is the documentation for a simple Django REST API project that allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource with a "name" attribute. This documentation provides details on how to use the API, including standard request and response formats, sample usage, limitations, and setup instructions.

## API Endpoints

### Create a User (POST)

**Endpoint:** `/api/`

**Request:**

```http
POST /api/
Content-Type: application/json

{
    "name": "John Doe"
}
```
## Response (Status 201 Created):
```
{
    "id": 1,
    "name": "John Doe"
}

```
## Retrieve a User by Name (GET)
** Endpoint: /api/?name={person_name} **
** Request: **
```
GET /api/?name=John%20Doe
```
## ** Response (Status 200 OK): **
```
[
    {
        "id": 1,
        "name": "John Doe"
    }
]

```
## Update a User (PUT/PATCH)
** Endpoint: /api/{person_name}/ **
** Request: **
```
PUT /api/John%20Doe/
Content-Type: application/json

{
    "name": "Updated Name"
}

```
** Response (Status 200 OK): **
```
{
    "id": 1,
    "name": "Updated Name"
}

```
## Delete a User (DELETE)
** Endpoint: /api/{person_name}/ **
** Request: **
```
DELETE /api/John%20Doe/

```
** Response (Status 204 No Content): **
No content returned.

## Limitations and Assumptions
- This API assumes that each person's name is unique.
- Only the "name" attribute is supported for CRUD operations.
- Error handling and validation may need improvement for production use.
## Setup and Deployment
Follow these steps to set up and deploy the API:
1. ** Clone this repository: **
```
https://github.com/NgBlaze/HNGx_Stage_2/
```
2. ** Navigate to the project directory: **
```
cd django-rest-api
```
3. ** Create a virtual environment and activate it: **
```
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

```
4. ** Install project dependencies: **
```
pip install -r requirements.txt

```
5. ** Apply database migrations: **
```
python manage.py migrate

```
6. ** Start the development server: **
```
python manage.py runserver

```

![UML_Image](https://github.com/NgBlaze/HNGx_Stage_2/blob/main/CRUD.drawio.png)


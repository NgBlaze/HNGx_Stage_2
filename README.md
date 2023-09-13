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

## **Response (Status 201 Created)**

    {
    "id": 1,
    "name": "John Doe"
}




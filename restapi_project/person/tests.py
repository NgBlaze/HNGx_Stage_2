from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person


class PersonAPITest(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()

        # Create test data
        self.person_data = {
            "name": "John Doe",
            "age": 30,
        }
        self.person = Person.objects.create(**self.person_data)

    def test_create_person(self):
        response = self.client.post(
            '/api/persons/', self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_person(self):
        response = self.client.get(f'/api/persons/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        updated_data = {
            "name": "Updated Name",
            "age": 35,
        }
        response = self.client.put(
            f'/api/persons/{self.person.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_person(self):
        updated_data = {
            "age": 40,
        }
        response = self.client.patch(
            f'/api/persons/{self.person.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        response = self.client.delete(f'/api/persons/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_person_by_name(self):
        response = self.client.get(f'/api/persons/{self.person.name}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_person_data(self):
        invalid_data = {
            "name": "John Doe",
            "age": "invalid_age",  # Invalid data type
        }
        response = self.client.post(
            '/api/persons/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

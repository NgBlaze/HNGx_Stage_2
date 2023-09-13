# myapi/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Person


class PersonAPITest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='John Doe')

    def test_get_person_by_id(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John Doe')

from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Employee


class EmployeeTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

        # Get tokens for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Authenticate the client
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Create an initial employee for testing
        self.employee = Employee.objects.create(
            email='jake@gmail.com',
            name='Jake',
            department='Engineering',
            role='Lead',
            date_joined='2024-11-03'
        )

    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_email(self):
        url = reverse('employee-list-create')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        url = reverse('employee-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_employees_by_department(self):
        Employee.objects.create(
            name='Alice', email='alice@example.com', department='HR')
        Employee.objects.create(
            name='Bob', email='bob@example.com', department='Engineering')
        url = reverse('employee-list-create') + '?department=HR'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)

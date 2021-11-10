from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo


class TestListCreateTodos(APITestCase):

    def authenticate(self):
        self.client.post(reverse("register"), {
            "username": "username", "email": "email@gmail.com",
            "password": "password"
        })

        response = self.client.post(
            reverse("login"), {"email": "email@gmail.com", "password": "password"}
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

    def test_should_not_creates_todo_with_no_auth(self):
        sample_todo = {"title": "hello", "desc": "Test"}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_creates_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate()
        sample_todo = {"title": "Hello", "desc": "Test"}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(Todo.objects.all().count(), previous_todo_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieves_all(self):
        self.authenticate()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        # sample_todo = {"title": "Hello", "desc": "Test"}
        # response = self.client.post(reverse('todos'), sample_todo)

        # res = self.client.get(reverse('todos'))
        # self.assertIsInstance(response.data['count'], int)
        # self.assertIsInstance(response.data['count'], 1)

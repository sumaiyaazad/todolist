from rest_framework.test import APITestCase
from authentication.models import User


# from .test_setup import TestSetup


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user(username="username", email="email@test.com", password="password1@212")
        self.assertEqual(user.username, "username")
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "email@test.com")
        self.assertIsInstance(user, User)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(username="username", email="email@test.com", password="password1@212")
        self.assertEqual(user.username, "username")
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.email, "email@test.com")
        self.assertIsInstance(user, User)

    def test_creates_super_user_with_is_staff(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username="username", email="email@test.com",
                          password="password1@212", is_staff=False)

        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                User.objects.create_superuser(is_staff=False, username="username", email="email@test.com",
                                              password="password1@212"))

    def test_creates_super_user_with_super_user_status(self):
        self.assertRaises(ValueError, User.objects.create_superuser, is_superuser=False, username="username",
                          email="email@test.com", password="password1@212")
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                User.objects.create_superuser(is_superuser=False, username="username", email="email@test.com",
                                              password="password1@212"))

    def test_cant_create_user_without_username(self):
        self.assertRaises(ValueError, User.objects.create_user, email="email@test.com",
                          password="password1@212", username="")

        with self.assertRaisesMessage(ValueError, 'Username must be set'):
            User.objects.create_user(email="email@test.com",
                                     password="password1@212", username="")

    def test_cant_create_user_without_email(self):
        self.assertRaises(ValueError, User.objects.create_user, email='',
                          password="password1@212", username="username")

        with self.assertRaisesMessage(ValueError, 'Email must be set'):
            User.objects.create_user(email='',
                                     password="password1@212", username="username")

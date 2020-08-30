from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_with_email_successful(self):
        """Test if creating a new user with an email is successful"""
        email = 'thomas.adams@enargit.org'
        password = 'testpwd12345687'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email of a new user is normalized"""
        email = 'thomas.adams@ENARGIT.COM'
        password = 'testpwd12345687'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """Test creating new user with no email raises error"""
        password = 'testpwd12345687'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password=password)

    def test_create_new_superuser(self):
        """"Test creating a new superuser"""
        email = 'thomas.adams@enargit.org'
        password = 'testpwd12345687'
        user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

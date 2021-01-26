from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelMangersTests(TestCase):
    def test_create_user_using_email_password(self):
        User = get_user_model()
        email = "test@gmail.com"
        password = "testpassword123"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        User = get_user_model()
        email = "test@GMAIL.COM"
        user = User.objects.create_user(email, "testpass")

        self.assertEqual(user.email, email.lower())

    def test_new_user_must_have_email(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(None, "testpass")

    def test_create_superuser(self):
        User = get_user_model()
        email = "test@gmail.com"
        password = "testpassword123"
        admin_user=User.objects.create_superuser(email=email,password=password)

        self.assertEqual(admin_user.email, email)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


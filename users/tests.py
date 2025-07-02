from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="vlad", email="cat@gmail.com", password="cat12345678910"
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(user.email, "cat@gmail.com")
        self.assertEqual(user.username, "vlad")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="vladik", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertEqual(admin_user.username, "vladik")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_login_user_by_username(self):
        get_user_model().objects.create_user(
            username="trofim", email="trofim@gmail.com", password="jsijf8f384"
        )
        can_login = self.client.login(username="trofim", password="jsijf8f384")
        self.assertTrue(can_login)

    def test_login_user_by_email(self):
        get_user_model().objects.create_user(
            username="trofim", email="trofim@gmail.com", password="jsijf8f384"
        )
        can_login = self.client.login(email="trofim@gmail.com", password="jsijf8f384")
        self.assertTrue(can_login)

from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='tester')
    def test_user_created(self):
        user = User.objects.filter(username='tester')
        self.assertTrue(user.exists())
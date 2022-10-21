from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status

User = get_user_model()


class UsersManagersTests(TestCase):

    def test_create_user(self):
        """Test to create a user through user model
        """
        user = User.objects.create_user(email='user@email.com', name='user', password='foo')
        self.assertEqual(user.email, 'user@email.com')
        self.assertEqual(user.name, 'user')
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', name='', password="foo")

    def test_create_superuser(self):
        """Test to create a superuser through user model
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', name='super', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.name, 'super')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='', name='', password='foo')


class AccountsTests(TestCase):

    def test_user_login(self):
        user = User.objects.create_user(email='user@email.com', name='user', password='foo')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'foo'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['refresh'])
        self.assertTrue(response.data['access'])

    def test_auth_user_register_with_all_fields(self):
        response = self.client.post(
            '/api/v1/auth/user/register/', {'email': 'test@email.com',
                                            'name': 'test', 'password': 'password@123', 're_password': 'password@123'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_auth_user_register_with_no_fields(self):
        response = self.client.post('/api/v1/auth/user/register/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {'email': ['This field is required.'],
                                                'name': ['This field is required.'],
                                                'password': ['This field is required.'],
                                                're_password': ['This field is required.']})

    def test_auth_user_register_with_one_field(self):
        response = self.client.post('/api/v1/auth/user/register/', {'email': 'test@email.com'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {'name': ['This field is required.'], 'password': [
                             'This field is required.'], 're_password': ['This field is required.']})

    def test_auth_user_register_with_short_password_field(self):
        response = self.client.post(
            '/api/v1/auth/user/register/', {'email': 'test@email.com', 'name': 'test',
                                            'password': 'foo', 're_password': 'foo'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {'password': [
                             'This password is too short. It must contain at least 8 characters.']})

    def test_auth_user_register_with_unequal_password_field(self):
        response = self.client.post(
            '/api/v1/auth/user/register/', {'email': 'test@email.com', 'name': 'test',
                                            'password': 'password@123', 're_password': 'passwor'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {'password': ["Password fields didn't match."]})

    def test_auth_get_user(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        response = self.client.get('/api/v1/auth/user/me/', **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_password(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        data = {'oldpassword': 'password@123', 'newpassword': 'password@1234'}
        response = self.client.put('/api/v1/auth/user/updatepassword/', data, **header, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_user_general_setting(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        data = {'email': 'normal@user.com', 'address': 'Kathmandu', 'phone': '9800654', 'mobile': '9800654', 'fblink': 'link', 'instalink': 'link'}
        response = self.client.put('/api/v1/auth/user/generalsetting/', data, **header, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from .models import UserData,TbSections


class RegisterAPITest(APITestCase):
    def test_register_user_No_username(self):
        
        url = reverse('register')
        data = {
            'username': '',
            'password': 'testpassword123',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['Error1'], "you can't register with empty username or password")
    
    def test_register_user_No_password(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': '',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['Error1'], "you can't register with empty username or password")
        
        
    def test_register_user_No_email(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email':"",
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['Error'], "Please enter your email to can log in")
        

    def test_register_user_successfully(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'],
                         'User created successfully,we send code to your email Please Verify your email')

    def test_register_user_with_short_username(self):
        url = reverse('register')
        data = {
            'username': 'test',
            'password': 'testpassword123',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['Error'],
                      'Username must be at least 5 characters long,and alphabet and numbers and not contain spaces.')

    def test_register_user_with_short_paasword(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'test12',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Password must be at least 8 characters long,and alphabet and numbers and not contain spaces.',
                      response.data['Error'])

    def test_register_user_with_invalid_password(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': '1234567',
            'email': 'testuser@example.com',
            'child_age': 5
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Password must be at least 8 characters long,and alphabet and numbers and not contain spaces.',
                      response.data['Error'])

    def test_register_user_without_child_age(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('User created successfully,we send code to your email Please Verify your email',
                      response.data['message'])


# class LoginTestCase(APITestCase):
#     def setUp(self):
#         self.sec=TbSections.objects.create(section_name="Pregnancy",child_age='Pregnancy')
#         self.user = User.objects.create_user('testuser', email='testuser@example.com', password='testpass@12')
#         self.user_data = UserData.objects.create(user=self.user, email_verified=True)
        
#     def test_login_with_child_age(self):
#         self.user_data.child_age ='Pregnancy'
#         self.user_data.save()
#         url = reverse('login')
#         data = {'username': 'test', 'password': 'testpass@12'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('User Login successfully', response.data['msg'])
#         self.assertIn('Pregnancy', response.data['section_choice'])
        
        
#     def test_login_with_valid_credentials(self):
#         url = reverse('login')
#         data = {'username': 'testuser', 'password': 'testpass@12'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('msg', response.data)

#     def test_login_with_invalid_credentials(self):
#         url = reverse('loginuser')
#         data = {'username': 'testuser', 'password': 'wrongword@12'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('username or password not existing', response.data['Error'])

#     def test_login_with_unverified_email(self):
#         self.user_data.email_verified = False
#         self.user_data.save()
#         url = reverse('login')
#         data = {'username': 'testuser', 'password': 'testpass@12'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('Please verify your email address before logging in.', response.data['error'])
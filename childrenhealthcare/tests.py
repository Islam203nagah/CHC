import pdb
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserData,TbSections,CustomAdmin
from django.core import mail

# class RegisterAPITest(APITestCase):
#     def test_register_user_No_username(self):
        
#         url = reverse('register')
#         data = {
#             'username': '',
#             'password': 'testpassword123',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn(response.data['Error1'], "you can't register with empty username or password")
    
#     def test_register_user_No_password(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': '',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn(response.data['Error1'], "you can't register with empty username or password")
        
        
#     def test_register_user_No_email(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword123',
#             'email':"",
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn(response.data['Error'], "Please enter your email to can log in")
        

#     def test_register_user_successfully(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword123',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['message'],
#                          'User created successfully,we send code to your email Please Verify your email')

#     def test_register_user_with_short_username(self):
#         url = reverse('register')
#         data = {
#             'username': 'test',
#             'password': 'testpassword123',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn(response.data['Error'],
#                       'Username must be at least 5 characters long,and alphabet and numbers and not contain spaces.')

#     def test_register_user_with_short_paasword(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': 'test12',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('Password must be at least 8 characters long,and alphabet and numbers and not contain spaces.',
#                       response.data['Error'])

#     def test_register_user_with_invalid_password(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': '1234567',
#             'email': 'testuser@example.com',
#             'child_age': 5
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('Password must be at least 8 characters long,and alphabet and numbers and not contain spaces.',
#                       response.data['Error'])

#     def test_register_user_without_child_age(self):
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword123',
#             'email': 'testuser@example.com',
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('User created successfully,we send code to your email Please Verify your email',
#                       response.data['message'])
# # import pdb
# class LoginUserTestCase(APITestCase):
#     def test_login_user_valid_credentials_verified_email(self):
#         username1 = "testuser"
#         password1 = "password123"
#         email_verified = True
#         # pdb.set_trace()
#         # create a User and UserData object with verified email
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.email_verified=email_verified
#         userdata.save()
        
#         # make a POST request to the loginuser endpoint
#         url = reverse('login')
#         data = {'username': 'testuser', 'password': 'password123'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 200 and the message indicates successful login
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['msg'],'User Login successfully')

#     def test_login_user_invalid_credentials(self):
#         username1 = "testuser"
#         password1 = "password123"
#         email_verified = True
#         # create a User and UserData object with verified email
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.email_verified=email_verified
#         userdata.save()
        
#         # make a POST request to the loginuser endpoint with invalid password
#         url = reverse('login')
#         data = {'username': username1, 'password': 'invalid_password'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 400 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data['Error'],'username or password not existing')
        
#     def test_login_user_email_not_verified(self):
#         username1 = "testuser"
#         password1 = "password123"
#         email_verified = False
#         # create a User and UserData object with not verified email
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.email_verified=email_verified
#         userdata.save()
        
#         # make a POST request to the loginuser endpoint with invalid password
#         url = reverse('login')
#         data = {'username': username1, 'password': password1}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 400 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data['error'],'Please verify your email address before logging in.')

    
#     def test_login_user_user_section(self):
#         username1 = "testuser"
#         password1 = "password123"
#         email_verified = True
#         # create a User and UserData and section object with verified email
#         useradmin = User.objects.create_user(username='islam', password='SUinfm@20320',is_staff=True)
#         cadmin=CustomAdmin.objects.create(user=useradmin)
#         createsec=TbSections.objects.create(admin_ID=cadmin,section_name='Pregnancy',child_age='Pregnancy')
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.child_age='Pregnancy'
#         userdata.email_verified=email_verified
#         userdata.save()
        
#         # make a POST request to the loginuser endpoint with invalid password
#         url = reverse('login')
#         data = {'username': username1, 'password': password1}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 400 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['msg'],'User Login successfully')
#         self.assertEqual(response.data['section_choice'],'Pregnancy')


# class VerifyEmailTestCase(APITestCase):
        

#     def test_verify_email_valid_code(self):
#         # make a POST request to the verify_email endpoint with valid code
#         username1 = "testuser"
#         password1 = "password123"
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.code_verification='qwerty'
#         userdata.save()
#         url = reverse('verifyemail')
#         data = {'code': 'qwerty'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 200 and the message indicates successful verification
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {'message': 'Email address verified.'})
        
#         # check that the email_verified flag is set to True in the database
#         userdata.refresh_from_db()
#         self.assertTrue(userdata.email_verified)
#         self.assertEqual(userdata.code_verification, '')

#     def test_verify_email_invalid_code(self):
#         # make a POST request to the verify_email endpoint with invalid code
#         username1 = "testuser"
#         password1 = "password123"
#         user = User.objects.create_user(username=username1, password=password1)
#         userdata=UserData.objects.filter(user=user.pk).first()
#         userdata.code_verification='qwerty'
#         userdata.save()
#         url =reverse('verifyemail')
#         data = {'code': 'ytrewq'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 400 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, {'error': 'Invalid verification code.'})
        
#         # check that the email_verified flag is still False in the database
#         userdata.refresh_from_db()
#         self.assertFalse(userdata.email_verified)
#         self.assertEqual(userdata.code_verification, 'qwerty')

#     def test_verify_email_missing_code(self):
#         # make a POST request to the verify_email endpoint without code
#         username1 = "testuser"
#         password1 = "password123"
#         user = User.objects.create_user(username=username1, password=password1)
#         user_data=UserData.objects.filter(user=user.pk).first()
#         user_data.code_verification='qwerty'
#         user_data.save()
#         url = reverse('verifyemail')
#         data = {'code':''}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 200 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, {'error': 'please enter code that send to your email'})
        
#         # check that the email_verified flag is still False in the database
#         user_data.refresh_from_db()
#         self.assertFalse(user_data.email_verified)
#         self.assertEqual(user_data.code_verification, 'qwerty')


# class ResetPasswordTestCase(APITestCase):

#     def test_reset_password_valid_email(self):
#         # make a POST request to the reset_password endpoint with valid email
#         user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
#         url = reverse('reset_password')
#         data = {'email': 'testuser@example.com'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 200 and the message indicates successful email sent
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {'message': 'Reset password code sent to your email address.'})
        
#         # check that a reset password email was sent to the user's email address
#         # pdb.set_trace()
#         outbox = mail.outbox
#         self.assertEqual(len(outbox), 1)
#         self.assertEqual(outbox[0].subject, 'Reset Your Password')
#         self.assertIn('Please enter the following code to reset your password:', outbox[0].body)

#     def test_reset_password_invalid_email(self):
#         # make a POST request to the reset_password endpoint with invalid email
#         user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
#         url = reverse('reset_password')
#         data = {'email': 'invalid@example.com'}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 404 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data, {'error': 'No user found with the provided email.'})
        
#         # check that no reset password email was sent
#         outbox = mail.outbox
        
#         self.assertEqual(len(outbox), 0)

#     def test_reset_password_missing_email(self):
#         # make a POST request to the reset_password endpoint without email
#         user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
#         url = reverse('reset_password')
#         data = {'email':''}
#         response = self.client.post(url, data, format='json')
        
#         # assert that the response status code is 404 and the error message is returned
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#         self.assertEqual(response.data, {'error': 'please enter a valid email'})
        
#         # check that no reset password email was sent
#         outbox = mail.outbox
#         self.assertEqual(len(outbox), 0)




# class ResetPasswordConfirmTestCase(APITestCase):


    # def setUp(self):
    #     self.user = User.objects.create_user(username='testuser',  password='password123')
    #     self.user_data = UserData.objects.create(user=self.user, code_verification='qwerty')
    #     self.url = reverse('')
    
    # def test_reset_password_confirm_success(self):
    #     username1 = "testuser"
    #     password1 = "password123"
    #     email1='testuser@example.com'
    #     user = User.objects.create_user(username=username1, email=email1,password=password1)
    #     user_data=UserData.objects.filter(user=user.pk).first()
    #     user_data.code_verification='qwerty'
    #     user_data.save()
    #     url = reverse('reset_password_confirm')
    #     data = {'code': 'qwerty', 'password': 'newpassword123'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {'message': 'Password reset successfully.'})
    #     self.assertTrue(User.objects.filter(username='testuser').first().check_password('newpassword123'))
    
    # def test_reset_password_confirm_invalid_code(self):
    #     username1 = "testuser"
    #     password1 = "password123"
    #     email1='testuser@example.com'
    #     user = User.objects.create_user(username=username1, email=email1,password=password1)
    #     user_data=UserData.objects.filter(user=user.pk).first()
    #     user_data.code_verification='qwerty'
    #     user_data.save()
    #     url = reverse('reset_password_confirm')
    #     data = {'code': 'ytrewq', 'password': 'newpassword123'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, {'error': 'Invalid reset password code.'})
    
    # def test_reset_password_confirm_invalid_password(self):
    #     username1 = "testuser"
    #     password1 = "password123"
    #     email1='testuser@example.com'
    #     user = User.objects.create_user(username=username1, email=email1,password=password1)
    #     user_data=UserData.objects.filter(user=user.pk).first()
    #     user_data.code_verification='qwerty'
    #     user_data.save()
    #     url = reverse('reset_password_confirm')
    #     data = {'code': 'qwerty', 'password': 'short'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data, {'error': 'please enter code that send to your email, and reset valid Password must be at least 8 characters long,and alphabet and numbers and not contain spaces.'})





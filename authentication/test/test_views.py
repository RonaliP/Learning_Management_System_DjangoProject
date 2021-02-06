from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserCreationSerializer
import json

CONTENT_TYPE = 'application/json'


class AuthenticationAPITest(TestCase):
    """ Test module for authentication APIs """

    def setUp(self):
        # initialize the APIClient app
        self.client = Client()

        self.admin = User.objects.create(username='admin',
                                         first_name='Rona',
                                         last_name='Panigrahy',
                                         email='Ronali@gmail.com',
                                         password='6767',
                                         role='Admin',
                                         is_superuser=True)
        self.student = User.objects.create(username='student',
                                           first_name='Sona',
                                           last_name='Panigrahy',
                                           email='student@gmail.com',
                                           password='898989',
                                           role='Student')
        self.mentor = User.objects.create(username='mentor',
                                          first_name='sahil',
                                          last_name='raj',
                                          email='mentor@gmail.com',
                                          password='0000',
                                          role='Mentor')

        self.user = User.objects.create(username='user',
                                        first_name='RonaliP',
                                        last_name='Panigrahy', role='Admin',
                                        email='rpanigrahy88@gmail.com',
                                        password='heyron')

        self.valid_user_payload = {
            'username': 'RonaliP',
            'first_name': 'Ronali',
            'last_name': 'Panigrahy',
            'email': 'ronalipanigrahy88@gmail.com@gmail.com',
            'mobile_number': '1234578688',
            'password': 'ronali',

        }

        self.invalid_user_payload = {
            'username': 'nmn',
            'first_name': 'Ronali',
            'last_name': '',
            'email': 'nbcbshxn',
            'password': 'ronali',
            'mobile_number': '1234567890',

        }
        self.admin_login_payload = {
            'username': 'admin',
            'password': '6767'
        }
        self.mentor_login_payload = {
            'username': 'mentor',
            'password': '0000'
        }
        self.student_login_payload = {
            'username': 'student',
            'password': '898989'
        }
        self.invalid_login_payload = {
            'username': 'hjhjhj',
            'password': 'jkjkj'
        }
        self.valid_reset_payload = {
            'email': 'Ronali@gmail.com'
        }
        self.invalid_reset_payload = {
            'email': ''
        }
        self.valid_new_password_payload = {
            'password': 'newpass',
            'confirm_password': 'newpass'
        }
        self.invalid_new_password_payload = {
            'password': 'newpass',
            'confirm_password': ''
        }

    ### Test cases for create-user API :

    def test_create_user_with_valid_payload_without_login(self):
        response = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.mentor_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_with_valid_payload_after_login_by_studnet_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.student_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ### Test cases to retrieve user-details API :

    def test_retrieve_user_details_with_valid_payload_without_login(self):
        response = self.client.get(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user_details_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.get(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user_details_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.get(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_details_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.mentor_login_payload), content_type=CONTENT_TYPE)
        response = self.client.get(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user_details_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.student_login_payload), content_type=CONTENT_TYPE)
        response = self.client.get(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ### Test cases to update user-details API :

    def test_user_details_with_valid_payload_without_login(self):
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.valid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_details_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.valid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_details_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.valid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_details_with_invalid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.invalid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_details_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.mentor_login_payload), content_type=CONTENT_TYPE)
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.valid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_details_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.student_login_payload), content_type=CONTENT_TYPE)
        response = self.client.put(reverse('user', kwargs={'id': self.admin.id}),
                                   data=json.dumps(self.valid_user_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ### Test cases to delete user-details API :

    def test_delete_user_with_valid_payload_without_login(self):
        response = self.client.delete(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.delete(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.delete(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.mentor_login_payload), content_type=CONTENT_TYPE)
        response = self.client.delete(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user_details_with_valid_payload_after_login_by_mentor_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.student_login_payload), content_type=CONTENT_TYPE)
        response = self.client.delete(reverse('user', kwargs={'id': self.admin.id}), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ### Test cases for login API :

    def test_login_with_superuser_credentials(self):
        response = self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_for_first_time_without_token(self):
        response = self.client.post(reverse('login'), data=json.dumps(self.student_login_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_for_first_time_with_token(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        test_user = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                     content_type=CONTENT_TYPE)
        token = test_user.data['token']
        test_user_payload = {
            'username': test_user.data['username'],
            'password': test_user.data['password'],
        }
        response = self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload),
                                    content_type=CONTENT_TYPE)
        user = User.objects.get(username=test_user.data['username'])
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEquals(user.first_login, True)

    def test_login_for_first_time_with_expired_token(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        test_user = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                     content_type=CONTENT_TYPE)
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImJoYXJ0aSIsImV4cCI6MTYxMjAxNTM2NSwiZW1haWwiOiJtYWxpYmhhcnRpNUBnbWFpbC5jb20ifQ.1MpnGpZUvuW_Nxuyk2O4Kc-H0plMnJQOTQ6-p7hgpHA'
        test_user_payload = {
            'username': test_user.data['username'],
            'password': test_user.data['password'],
        }
        response = self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_for_first_time_with_invalid_token(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        test_user = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                     content_type=CONTENT_TYPE)
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1c2VybmFtZSI6ImJoYXJ0aSIsImV4cCI6MTYxMjAxNTM2NSwiZW1haWwiOiJtYWxpYmhhcnRpNUBnbWFpbC5jb20ifQ.1MpnGpZUvuW_Nxuyk2O4Kc-H0plMnJQOTQ6-p7hgpHA'
        test_user_payload = {
            'username': test_user.data['username'],
            'password': test_user.data['password'],
        }
        response = self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_for_second_time_with_token(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        test_user = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                     content_type=CONTENT_TYPE)
        token = test_user.data['token']
        test_user_payload = {
            'username': test_user.data['username'],
            'password': test_user.data['password'],
        }
        self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload), content_type=CONTENT_TYPE)
        self.client.get(reverse('logout'), content_type=CONTENT_TYPE)
        response = self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload),
                                    content_type=CONTENT_TYPE)
        user = User.objects.get(username=test_user.data['username'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(user.first_login, True)

    def test_login_for_second_time_without_token(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        test_user = self.client.post(reverse('create-user'), data=json.dumps(self.valid_user_payload),
                                     content_type=CONTENT_TYPE)
        token = test_user.data['token']
        test_user_payload = {
            'username': test_user.data['username'],
            'password': test_user.data['password'],
        }
        self.client.post('/auth/login/?token=' + token, data=json.dumps(test_user_payload), content_type=CONTENT_TYPE)
        self.client.get(reverse('logout'), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('login'), data=json.dumps(test_user_payload), content_type=CONTENT_TYPE)
        user = User.objects.get(username=test_user.data['username'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(user.first_login, True)

    ### Test cases for Reset-password :

    def test_reset_password_with_valid_payload_without_login(self):
        response = self.client.post(reverse('reset-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_reset_password_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('reset-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_reset_password_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('reset-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_password_with_invalid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('reset-password'), data=json.dumps(self.invalid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reset_password_of_other_user_with_valid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('reset-password'), data=json.dumps({'email': 'student@gmail.com'}),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reset_password_by_using_wrong_email_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('reset-password'), data=json.dumps({'email': 'students@gmail.com'}),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ### Test cases for Forgot-password :

    def test_forgot_password_with_valid_payload_without_login(self):
        response = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forgot_password_with_valid_payload_after_login_by_invalid_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.invalid_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forgot_password_with_valid_payload_after_login_by_admin_credentials(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forgot_password_with_invalid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        response = self.client.post(reverse('forgot-password'), data=json.dumps(self.invalid_reset_payload),
                                    content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    ### Test cases for new-password :

    def test_new_password_with_valid_payload_without_login(self):
        res = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                               content_type=CONTENT_TYPE)
        token = res.data['token']
        response = self.client.put('/auth/new-password/?token=' + token,
                                   data=json.dumps(self.valid_new_password_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_password_for_reset_password_with_valid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        res = self.client.post(reverse('reset-password'), data=json.dumps(self.valid_reset_payload),
                               content_type=CONTENT_TYPE)
        token = res.data['token']
        response = self.client.put('/auth/new-password/?token=' + token,
                                   data=json.dumps(self.valid_new_password_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_password_for_forgot_password_with_valid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        res = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                               content_type=CONTENT_TYPE)
        token = res.data['token']
        response = self.client.put('/auth/new-password/?token=' + token,
                                   data=json.dumps(self.valid_new_password_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_password_with_invalid_payload_after_login(self):
        self.client.post(reverse('login'), data=json.dumps(self.admin_login_payload), content_type=CONTENT_TYPE)
        res = self.client.post(reverse('forgot-password'), data=json.dumps(self.valid_reset_payload),
                               content_type=CONTENT_TYPE)
        token = res.data['token']
        response = self.client.put('/auth/new-password/?token=' + token,
                                   data=json.dumps(self.invalid_new_password_payload), content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
from rest_framework.test import APITestCase

from .models import User

class UserTokenObtainAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

    def setUp(self):
        self.create_user()
        self.url_login = '/login/'
        self.url_test_token = '/api/test_token/'

    def tearDown(self):
        User.objects.all().delete()

    def test_user_login(self):
        user_credentials = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha no login de usuário'
        )

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def test_wrong_credentials_login(self):
        wrong_credentials = {
            'email': 'luis@teste',
            'password': 'luis'
        }

        response = self.client.post(
            self.url_login,
            wrong_credentials,
            format='json'
        )

        self.assertEqual(response.status_code, 401, msg='Login com credenciais corretas')

    def test_token_validator(self):
        self.test_user_login()

        response = self.client.get(
            self.url_test_token,
            format='json',
            **self.auth_token
        )

        self.assertEqual(response.status_code, 200, msg='Token inválido')

    def test_invalid_token_validator(self):
        self.test_user_login()
        
        invalid_token = {'HTTP_AUTHORIZATION': 'Bearer invalid'}
        
        response = self.client.get(
            self.url_test_token,
            format='json',
            **invalid_token
        )

        self.assertEqual(response.status_code, 401, msg='Token válido')
        self.assertEqual(response.json()['detail'], 'Given token not valid for any token type', msg='Token válido')

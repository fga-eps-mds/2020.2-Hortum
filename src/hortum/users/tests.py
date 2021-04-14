from rest_framework.test import APITestCase

from ..users.models import User
from ..customer.models import Customer

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

    def tearDown(self):
        Customer.objects.all().delete()

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

        self.assertEqual(
            response.status_code,
            401,
            msg='Login com credenciais incorretas'
        )

class UpdateUserViewTestCase(APITestCase):
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
    
    def create_tokens(self):
        user_cred = {'email': self.user_data['email'], 'password': self.user_data['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}
        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.url_login = '/login/'
        self.url_update_user = '/users/update/'

    def test_change_existent_email(self):
        other_user_data = {
            'username': 'Marcos Segundo',
            'email': 'marcos@productor.com',
            'password': 'teste dois'
        }
        
        user_username_email = {
	        "username": self.user_data['email'],
            "email": "marcos@productor.com"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
            {'user': other_user_data},
            format='json'
        )

        response = self.client.put(
            path=self.url_update_user,
            data=user_username_email,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 401, msg='Email nao existente')

    def test_update_user(self):
        user_username_email = {
	        "username": "Luis2",
            "email": "luis2@productor.com"
        }

        response =  self.client.put(
            path=self.url_update_user,
            data=user_username_email,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 200, msg='Usuario nao atualizado')
    
    def test_empty_update_user(self):
        response =  self.client.put(
            path=self.url_update_user,
            data={},
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Campos nao vazios')
    
    def test_user_login_old_email(self):
        self.test_update_user()
        user_credentials = {
            'email': "luis@productor.com",
            'password': self.user_data['password']
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Login com credenciais incorretas'
        )
        
    def test_user_login_new_email(self):
        self.test_update_user()
        user_credentials = {
            'email': "luis2@productor.com",
            'password': self.user_data['password'],
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

    def tearDown(self):
        Customer.objects.all().delete()
        User.objects.all().delete()

class ChangePasswordViewTestCase(APITestCase):
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
    
    def create_tokens(self):
        user_cred = {'email': self.user_data['email'], 'password': self.user_data['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}
        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.url_login = '/login/'
        self.url_change_password = '/users/change-password/'

    def test_wrong_old_password(self):
        user_password = {
	        "old_password": "asdsd",
            "new_password": "gfdfgdgffg"
        }

        response = self.client.put(
            path=self.url_change_password,
            data=user_password,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 401, msg='Senha correta inserida')

    def test_change_password(self):
        user_password = {
	        "old_password": "teste",
            "new_password": "nova senha"
        }

        response =  self.client.put(
            path=self.url_change_password,
            data=user_password,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 200, msg='Senha nao alterada')
    
    def test_user_login_old_password(self):
        self.test_change_password()
        user_credentials = {
            'email': self.user_data['email'],
            'password': "teste"
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Login com credenciais incorretas'
        )
        
    def test_user_login_new_password(self):
        self.test_change_password()
        user_credentials = {
            'email': self.user_data['email'],
            'password': "nova senha",
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

    def test_empty_password_fields(self):
        response =  self.client.put(
            path=self.url_change_password,
            data={},
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Campos nao vazios')
        
    def tearDown(self):
        Customer.objects.all().delete()
        User.objects.all().delete()
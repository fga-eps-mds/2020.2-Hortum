from rest_framework.test import APITestCase

from .models import Productor

class ProductorRegisterAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Marcos',
            'email': 'marcos@productor.com',
            'password': 'teste'
        }

        self.url_signup = '/signup/productor/'

    def tearDown(self):
        Productor.objects.all().delete()

    def test_productor_register(self):
        response = self.client.post(
            self.url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.assertEqual(
            response.status_code,
            201,
            msg='Falha no registro de produtor'
        )

    def test_duplicate_email_register(self):
        other_user_data = {
            'username': 'Marcos Segundo',
            'email': 'marcos@productor.com',
            'password': 'teste dois'
        }

        self.client.post(
            self.url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        response = self.client.post(
            self.url_signup,
            {'user': other_user_data},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            400,
            msg='Registro com email repetido'
        )

    def test_empty_field_register(self):
        incomplete_user_data = {
            'username': 'Marcos Terceiro',
            'email': '',
            'password': ''
        }

        response = self.client.post(
            self.url_signup,
            incomplete_user_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            400,
            msg='Registro com campos vazios'
        )

class ProductorListAPIViewTestCase(APITestCase):
    def create_productor(self):
        self.user_data = {
	        "username": "Luigi",
            "email": "luigi@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
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

    def setUp(self):
        self.create_productor()
        self.create_tokens()
        self.url_list = '/productor/list/'

    def tearDown(self):
        Productor.objects.all().delete()

    def test_list_productors(self):
        response = self.client.get(
            self.url_list,
            **self.auth_token
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha ao listar produtores'
        )

    def test_list_productors_no_authentication(self):
        response = self.client.get(
            self.url_list,
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Listando produtores sem autenticação'
        )


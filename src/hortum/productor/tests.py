from rest_framework.test import APITestCase

from .models import Productor
from ..customer.models import Customer
from ..encode import encode_string

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

class ProductorRetrieveAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Marcelo",
            "email": "marcelo@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )
        
        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')

    def create_productors(self):
        productors_data = [
            {
                'username': 'João',
                'email': 'joao@productor.com',
                'password': 'teste'
            },
            {
                'username': 'Mario',
                'email': 'mario@productor.com',
                'password': 'teste'
            }
        ]

        url_signup = '/signup/productor/'

        for prod_data in productors_data:
            response = self.client.post(
                url_signup,
                {'user': prod_data},
                format='json'
            )
            self.assertEqual(response.status_code, 201, msg='Falha na criação de outros produtores')
        
    def create_tokens(self):
        user_cred = {'email': self.user_data['email'], 'password': self.user_data['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.assertEqual(response.status_code, 200, msg='Credenciais inválidas')

        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def setUp(self):
        self.create_user()
        self.create_productors()
        self.create_tokens()
        self.url_retrieve = '/productor/retrieve/'

    def tearDown(self):
        Productor.objects.all().delete()
        Customer.objects.all().delete()

    def test_retrieve_productor(self):
        email_query = 'joao@productor.com'
        url_retrieve_productor = self.url_retrieve + encode_string(email_query) + '/'

        response = self.client.get(
            url_retrieve_productor,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na obtenção de produtor específico')
        self.assertEqual(response.data['username'], 'João', msg='Dados de produtor estão incoerentes')

    def test_invalid_email(self):
        email_query = 'luigi@teste.com'
        url_retrieve_productor = self.url_retrieve + encode_string(email_query) + '/'

        response = self.client.get(
            url_retrieve_productor,
            **self.creds
        )

        self.assertEqual(response.status_code, 404, msg='Retornando produtor com email inválido')

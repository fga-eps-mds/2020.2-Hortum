from rest_framework.test import APITestCase

from .models import Productor
from ..customer.models import Customer
from ..encode import encode_string

class ProductorRegisterAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Marcos',
            'email': 'marcos@productor.com',
            'password': 'teste',
            'phone_number': '61123456757',
            'is_verified': True
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

    def test_empty_attr_register_productor(self):
        response = self.client.post(
            self.url_signup,
            {'user': {}},
            format='json'
        )

        self.assertEqual(response.status_code, 400, msg='User possível de se criar')
        self.assertEqual(len(response.json()['user']), 3, msg='Pelo menos um campo é necessário')

    def test_duplicate_email_register_productor(self):
        self.test_productor_register()

        new_user = {
            'username': 'Marcos Segundo',
            'email': 'marcos@productor.com',
            'password': 'teste dois',
            'phone_number': '51123456787',
            'is_verified': True
        }

        response = self.client.post(
            self.url_signup,
            {'user': new_user},
            format='json'
        )
        
        self.assertEqual(response.status_code, 400, msg='Email inexistente')

class ProductorListAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            'username': 'Marcos',
            'email': 'marcos@productor.com',
            'password': 'teste',
            'phone_number': '61123456787',
            'is_verified': True
        }

        url_signup = '/signup/productor/'

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
                'password': 'teste',
                'phone_number': '61123456786',
                'is_verified': True
            },
            {
                'username': 'Mario',
                'email': 'mario@productor.com',
                'password': 'teste',
                'phone_number': '61123456785',
                'is_verified': True
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
        user_credentials = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(response.status_code, 200, msg='Credenciais inválidas')

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def setUp(self):
        self.create_user()
        self.create_productors()
        self.create_tokens()
        self.url_list = '/productor/list/'

    def tearDown(self):
        Productor.objects.all().delete()

    def test_list_all_productors(self):
        response = self.client.get(
            self.url_list,
            **self.auth_token
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores')
        self.assertEqual(len(response.data), 3, msg='Falha na quantidade de produtores listados')

    def test_search_productors(self):
        url_search = self.url_list + 'mar/'

        response = self.client.get(
            url_search,
            **self.auth_token
        )

        self.assertEqual(response.status_code, 200, msg='Falha na busca de produtores')
        self.assertEqual(len(response.data), 2, msg='Falha na quantidade de produtores listados na pesquisa')

    def test_only_productors_are_listed(self):
        customer_data = {
            'username': 'Customer',
            'email': 'customer@customer.com',
            'password': 'teste',
            'phone_number': '61123456783',
            'is_verified': True
        }

        url_signup_customer = '/signup/customer/'

        response = self.client.post(
            url_signup_customer,
            {'user': customer_data},
            format='json'
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de comprador')

        response = self.client.get(
            self.url_list,
            **self.auth_token
        )
        
        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores')
        self.assertEqual(len(response.data), 3, msg='Quantidade de produtores errada')
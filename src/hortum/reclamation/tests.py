from rest_framework.test import APITestCase

from ..reclamation.models import Reclamation
from ..customer.models import Customer
from ..productor.models import Productor
from ..users.models import User

class ReclamationRegistrationAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            "username": "Jose",
            "email": "customer@teste.com",
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

        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}
    
    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.url_login = '/login/'
        self.url_register_reclamation = '/reclamation/create/'

    def register_productor(self):
        productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

    def test_register_reclamation(self):
        self.register_productor()

        reclamation_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 201, msg="Falha ao registrar reclamação")

    def test_register_reclamation_again(self):
        self.register_productor()
        reclamation_data = {
            'author': "Jose",
            'description': "produtor do perfeito",
            'emailProductor': "productor@teste.com"
        }

        self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        response = self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg="Registro de mais de uma reclamação realizada com sucesso")

    def test_empty_fields(self):
        self.register_productor()
        
        response = self.client.post(
            path=self.url_register_reclamation,
            data={},
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg="Registro de reclamação com campos vazios")

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()

class ReclamationListAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            "username": "Jose",
            "email": "customer@teste.com",
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

        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}
    
    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.url_login = '/login/'
        self.url_register_reclamation = '/reclamation/create/'
        self.url_list_reclamations = '/reclamation/list/'

    def test_list_reclamation(self):
        productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        reclamation_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        encodedEmail = 'cHJvZHVjdG9yQHRlc3RlLmNvbQ=='

        response = self.client.get(
            path=self.url_list_reclamations+encodedEmail,
            **self.creds,
            follow=True
        )


        self.assertEqual(response.status_code, 200, msg="Falha ao listar reclamações")

    def test_list_reclamation_empty(self):
        productor_data = {
            "username": "Marcio",
            "email": "productor2@teste.com",
	        "password": "teste2"
        }

        url_signup = '/signup/productor/'

        self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        encodedEmail = 'cHJvZHVjdG9yMkB0ZXN0ZS5jb20='

        response = self.client.get(
            path=self.url_list_reclamations+encodedEmail,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg="Falha ao listar produtor sem reclamações")

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()


    


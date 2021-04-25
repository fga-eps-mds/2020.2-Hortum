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

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )
    
        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')

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

    def register_productor(self):
        productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')
    
    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.register_productor()
        self.url_login = '/login/'
        self.url_register_reclamation = '/reclamation/create/'

    def test_register_reclamation(self):
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
        reclamation_data = {
            'author': "Jose",
            'description': "produtor do perfeito",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha no registro de reclamação')

        response = self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg="Registro de mais de uma reclamação realizada com sucesso")

    def test_empty_fields(self):
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
        Reclamation.objects.all().delete()
        User.objects.all().delete()

class ReclamationListAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            "username": "Jose",
            "email": "customer@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')
    
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

    def register_productor(self):
        productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')
    
    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.register_productor()
        self.url_login = '/login/'
        self.url_register_reclamation = '/reclamation/create/'
        encodedEmail = 'cHJvZHVjdG9yQHRlc3RlLmNvbQ=='
        self.url_list_reclamations = '/reclamation/list/' + encodedEmail
        
    def test_list_reclamation(self):
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

        self.assertEqual(response.status_code, 201, msg='Falha ao registrar reclamação')

        response = self.client.get(
            path=self.url_list_reclamations,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg="Falha ao listar reclamações")

    def test_list_reclamation_empty(self):
        response = self.client.get(
            path=self.url_list_reclamations,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg="Falha ao listar produtor sem reclamações")

    def test_list_reclamation_non_existent_productor(self):
        emailNonExistentProductor = 'cHJvZHVjdG9yMjNAZ21haWwuY29t'

        response = self.client.get(
            path='/reclamation/list/' + emailNonExistentProductor,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 400, msg='Listou reclamações de produtor não existente')

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Reclamation.objects.all().delete()
        User.objects.all().delete()

class ReclmationDeleteAPIViewTestCase(APITestCase):
    def create_admin(self):
        admin = User(username='admin', email='admin@teste.com', is_staff=True)
        admin.set_password('test')
        admin.save()
        self.admin_data = {
            "email": 'admin@teste.com',
	        "password": 'test'
        }

    def create_tokens(self, user_data):
        user_cred = {'email': user_data['email'], 'password': user_data['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.assertEqual(response.status_code, 200, msg='Credenciais inválidas')

        creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

        return creds

    def setUp(self):
        self.create_admin()
        self.creds = self.create_tokens(user_data=self.admin_data)
        self.url_login = '/login/'
        self.url_delete_reclamation = '/reclamation/delete/'
        self.url_register_reclamation = '/reclamation/create/'

    def register_productor(self):
        self.productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': self.productor_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')

    def register_customer(self):
        self.customer_data = {
            "username": "Jose",
            "email": "customer@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.customer_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha no signup de customer')

    def register_reclamation(self):
        self.register_productor()

        self.register_customer()

        creds = self.create_tokens(user_data=self.customer_data)

        reclamation_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_reclamation,
            data=reclamation_data,
            format='json',
            **creds,
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de reclamação')

    def test_delete_reclamation(self):
        self.register_reclamation()

        emailCustomer = 'Y3VzdG9tZXJAdGVzdGUuY29t/'

        delete_data = {
            'emailProductor': self.productor_data['email']
        }

        response = self.client.delete(
            path=self.url_delete_reclamation + emailCustomer,
            data=delete_data,
            format='json',
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg='Falha na deleção de reclamação')

    def test_delete_non_existent_reclamation(self):
        self.register_productor()

        self.register_customer()

        emailCustomer = 'Y3VzdG9tZXJAdGVzdGUuY29t/'

        delete_data = {
            'emailProductor': self.productor_data['email']
        }

        response = self.client.delete(
            path=self.url_delete_reclamation + emailCustomer,
            data=delete_data,
            format='json',
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 400, msg='Reclamação não existente deletada')

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Reclamation.objects.all().delete()
        User.objects.all().delete()

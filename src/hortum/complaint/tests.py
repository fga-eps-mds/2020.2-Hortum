import os
import io

from PIL import Image

from rest_framework.test import APITestCase

from django.conf import settings

from ..complaint.models import Complaint
from ..customer.models import Customer
from ..productor.models import Productor
from ..users.models import User

class ComplaintRegistrationAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            "username": "Jose",
            "email": "customer@teste.com",
	        "password": "teste",
            'phone_number': '61123456787'
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        User.objects.filter(email=self.user_data['email']).update(is_verified=True)
    
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
	        "password": "teste",
            'phone_number': '62123456787'
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        User.objects.filter(email=productor_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')
    
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.register_productor()
        self.url_login = '/login/'
        self.url_register_complaint = '/complaint/create'

    def test_register_Complaint(self):
        complaint_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 201, msg="Falha ao registrar reclamação")

    def test_register_Complaint_with_photo(self):
        photo_file = self.generate_photo_file()
        complaint_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com",
            'image': photo_file
        }

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='multipart',
            **self.creds
        )

        expected = Complaint.upload_image(Complaint.objects.get(author=complaint_data['author']), photo_file.name)
        self.assertEqual(response.status_code, 201, msg="Falha ao registrar reclamação")
        self.assertEqual(response.data['image'], 'http://testserver/images/' + expected, msg='Falha no link da foto')

    def test_register_complaint_again(self):
        complaint_data = {
            'author': "Jose",
            'description': "produtor do perfeito",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha no registro de reclamação')

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg="Registro de mais de uma reclamação realizada com sucesso")

    def test_empty_fields(self):
        response = self.client.post(
            path=self.url_register_complaint,
            data={},
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg="Registro de reclamação com campos vazios")

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Complaint.objects.all().delete()
        User.objects.all().delete()
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name != 'person-male.png':
                    os.remove(root + '/' + name)

class ComplaintListAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
            "username": "Jose",
            "email": "customer@teste.com",
	        "password": "teste",
            'phone_number': '63123456787'
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        User.objects.filter(email=self.user_data['email']).update(is_verified=True)

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
	        "password": "teste",
            'phone_number': '64123456787'
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': productor_data},
	        format='json'
	    )

        User.objects.filter(email=productor_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')
    
    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.register_productor()
        self.url_login = '/login/'
        self.url_register_complaint = '/complaint/create'
        self.url_list_complaints = '/complaint/list/'
        
    def test_list_complaint(self):
        complaint_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha ao registrar reclamação')

        self.url_list_complaints += 'cHJvZHVjdG9yQHRlc3RlLmNvbQ=='

        response = self.client.get(
            path=self.url_list_complaints,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg="Falha ao listar reclamações")

    def test_list_complaint_empty(self):
        self.url_list_complaints += 'cHJvZHVjdG9yQHRlc3RlLmNvbQ=='
        response = self.client.get(
            path=self.url_list_complaints,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg="Falha ao listar produtor sem reclamações")

    def test_list_complaint_invalid_url(self):
        response = self.client.get(
            path=self.url_list_complaints,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 400, msg='Reclamações listadas com sucesso')

    def test_list_complaint_non_existent_productor(self):
        emailNonExistentProductor = 'cHJvZHVjdG9yMjNAZ21haWwuY29t'

        response = self.client.get(
            path='/complaint/list/' + emailNonExistentProductor,
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 400, msg='Listou reclamações de produtor não existente')

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Complaint.objects.all().delete()
        User.objects.all().delete()

class ComplaintDeleteAPIViewTestCase(APITestCase):
    def create_admin(self):
        admin = User(username='admin', email='admin@teste.com', is_verified=True, is_staff=True)
        admin.set_password('test')
        admin.save()
        self.admin_data = {
            'email': 'admin@teste.com',
	        'password': 'test'
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
        self.url_delete_Complaint = '/complaint/delete/'
        self.url_register_complaint = '/complaint/create'

    def register_productor(self):
        self.productor_data = {
            "username": "Raimundo",
            "email": "productor@teste.com",
	        "password": "teste",
            'phone_number': '65123456787'
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': self.productor_data},
	        format='json'
	    )

        User.objects.filter(email=self.productor_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha no signup de productor')

    def register_customer(self):
        self.customer_data = {
            "username": "Jose",
            "email": "customer@teste.com",
	        "password": "teste",
            'phone_number': '66123456787'
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.customer_data},
	        format='json'
	    )

        User.objects.filter(email=self.customer_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha no signup de customer')

    def register_complaint(self):
        self.register_productor()

        self.register_customer()

        creds = self.create_tokens(user_data=self.customer_data)

        complaint_data = {
            'author': "Jose",
            'description': "produtor do bom",
            'emailProductor': "productor@teste.com"
        }

        response = self.client.post(
            path=self.url_register_complaint,
            data=complaint_data,
            format='json',
            **creds,
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de reclamação')

    def test_delete_complaint(self):
        self.register_complaint()

        emailCustomer = 'Y3VzdG9tZXJAdGVzdGUuY29t'

        delete_data = {
            'emailProductor': self.productor_data['email']
        }

        response = self.client.delete(
            path=self.url_delete_Complaint + emailCustomer,
            data=delete_data,
            format='json',
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 200, msg='Falha na deleção de reclamação')

    def test_delete_non_existent_Complaint(self):
        self.register_productor()

        self.register_customer()

        emailCustomer = 'Y3VzdG9tZXJAdGVzdGUuY29t'

        delete_data = {
            'emailProductor': self.productor_data['email']
        }

        response = self.client.delete(
            path=self.url_delete_Complaint + emailCustomer,
            data=delete_data,
            format='json',
            **self.creds,
            follow=True
        )

        self.assertEqual(response.status_code, 400, msg='Reclamação não existente deletada')

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Complaint.objects.all().delete()
        User.objects.all().delete()
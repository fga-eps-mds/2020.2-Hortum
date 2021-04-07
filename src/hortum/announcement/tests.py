from rest_framework.test import APITestCase

from ..productor.models import Productor
from ..users.models import User
from .models import Announcement

class AnnouncementsDeleteUpdateAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	    "username": "João",
            "email": "joao@teste.com",
	    "password": "teste"
        }

        url_signup = '/signup/productor/'

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

    def create_announcement(self):
        self.announcement_data = {
            "email": self.user_data['email'],
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50
        }

        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	    data=self.announcement_data,
	    format='json',
	    **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.create_announcement()

        self.url_update_announ = '/announcement/update/' + self.announcement_data['name']

    def tearDown(self):
        Announcement.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()

    def test_delete_announcement(self):
        response = self.client.delete(
            path=self.url_update_announ,
	    format='json',
	    **self.creds
        )

        self.assertEqual(response.status_code, 204, msg='Falha na deleção do anúncio')

    def test_update_one_attr_announcement(self):
        new_data = {
            "name": "Meio quilo de defumados"
        }

        response = self.client.patch(
            path=self.url_update_announ,
	    format='json',
	    data=new_data,
	    **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração do anúncio')

    def test_update_multiples_attr_announcement(self):
        new_data = {
            "name": "Meio quilo de defumados",
	    "description": "Defumados",
	    "price": 60.15
        }

        response = self.client.patch(
            path=self.url_update_announ,
	    format='json',
	    data=new_data,
	    **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração do anúncio')

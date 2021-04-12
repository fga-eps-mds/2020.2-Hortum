from rest_framework.test import APITestCase

from ..productor.models import Productor
from ..users.models import User
from .models import Announcement

class AnnouncementCreateAPIViewTestCase(APITestCase):
    def create_productor(self):
        self.user_data = {
	        "username": "Mário",
            "email": "mario@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

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

    def setUp(self):
        self.create_productor()
        self.create_tokens()
        self.announcement_data = {
            "name": "Banana",
            "type_of_product": "Banana",
            "description": "vendendo banana",
            "price": 10.0
        }
        self.url_announcement = '/announcement/create'

    def test_create_announcement(self):
        response = self.client.post(
            self.url_announcement,
            self.announcement_data,
            format='json',
            **self.auth_token
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Falha na criação de anúncio'
        )

    def test_duplicate_announcement_name(self):
        other_announcement = {
            "name": "Banana",
            "type_of_product": "Banana",
            "description": "banana à venda",
            "price": 12.5
        }

        self.client.post(
            self.url_announcement,
            self.announcement_data,
            format='json',
            **self.auth_token
        )

        response = self.client.post(
            self.url_announcement,
            other_announcement,
            format='json',
            **self.auth_token
        )

        self.assertEqual(
            response.status_code,
            400,
            msg='Criando anúncio com nome duplicado'
        )

    def test_create_announcement_no_authentication(self):
        response = self.client.post(
            self.url_announcement,
            self.announcement_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Criando anúncio sem autenticação'
        )

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

class AnnouncementsListAPIViewTestCase(APITestCase):
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
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50
        }
    
        self.announcement_data_extra = {
            "name": "Meio quilo de defumado",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Defumados",
            "price": 10.15
        }

        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_data,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_data_extra,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

    def change_inventory(self):
        new_data = {
            "inventory": False
        }

        url_update_announ = '/announcement/update/' + self.announcement_data['name']

        response = self.client.patch(
            path=url_update_announ,
	        format='json',
	        data=new_data,
	        **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração do anúncio')

    def setUp(self):
        self.create_user()
        self.create_tokens()
        self.create_announcement()

        self.url_list_announ = '/announcement/list'

    def tearDown(self):
        Announcement.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()

    def test_list_all_true_announcement(self):
        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem do anúncio')
        self.assertEqual(len(response.data), 2, msg='Falha na quantidade de anúncios listados')
    
    def test_list_false_inventory_announcement(self):
        self.change_inventory()

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem do anúncio')
        self.assertEqual(len(response.data), 1, msg='Falha na quantidade de anúncios listados')
    
    def test_list_names_multiples_annoucement(self):
        self.url_list_announ += '/Meio'

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio com o nome inserido')
        self.assertEqual(len(response.data), 2, msg='Falha na quantidade de anúncios listados')

    def test_list_names_one_announcement(self):
        self.url_list_announ += '/Meio quilo de linguíça'

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 1, msg='Falha na busca por anúncio')

    def test_list_containing_name_announcement(self):
        self.url_list_announ += '/quilo de'

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 2, msg='Falaha na busca por anúncio')
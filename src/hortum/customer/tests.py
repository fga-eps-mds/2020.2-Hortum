from rest_framework.test import APITestCase

from .models import Customer
from ..productor.models import Productor
from ..announcement.models import Announcement

class CustomerRegisterAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Pedro',
            'email': 'pedro@customer.com',
            'password': 'teste'
        }

        self.url_signup = '/signup/customer/'

    def tearDown(self):
        Customer.objects.all().delete()

    def test_customer_register(self):
        response = self.client.post(
            self.url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.assertEqual(response.status_code, 201, msg='Falha no registro de comprador')

    def test_empty_attr_register_customer(self):
        response = self.client.post(
            self.url_signup,
            {'user': {}},
            format='json'
        )

        self.assertEqual(response.status_code, 400, msg='User possível de se criar')
        self.assertEqual(len(response.json()['user']), 3, msg='Pelo menos um campo é necessário')

    def test_duplicate_email_register_customer(self):
        self.test_customer_register()

        new_user = {
            'username': 'João',
            'email': 'pedro@customer.com',
            'password': 'teste'
        }
        
        response = self.client.post(
            self.url_signup,
            {'user': new_user},
            format='json'
        )

        self.assertEqual(response.status_code, 400, msg='Email inexistente')

class CustomerFavoritesAPIViewTestCase(APITestCase):
    def create_productor(self):
        self.productor_data = {
	        "username": "Mário",
            "email": "mario@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        self.client.post(
            url_signup,
	        {'user': self.productor_data},
	        format='json'
	    )

    def create_tokens(self, user):
        user_cred = {'email': user['email'], 'password': user['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def create_customer(self):
        self.customer_data = {
	        "username": "João Pedro",
            "email": "joao@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.customer_data},
	        format='json'
	    )

    def create_announcements(self):
        self.announcement_one = {
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50,
            "localizations": [],
        }
    
        self.announcement_two = {
            "name": "Meio quilo de defumado",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Defumados",
            "price": 10.15,
            "localizations": [],
        }

        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_one,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_two,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

    def setUp(self):
        self.create_productor()
        self.create_tokens(self.productor_data)
        self.create_announcements()
        self.create_customer()
        self.create_tokens(self.customer_data)

        self.announcement_fav_url = '/customer/fav-announcement'
        self.productor_fav_url = '/customer/fav-productor'
        self.list_fav_announcements_url = '/customer/favorites/announcements'
        self.list_fav_productors_url = '/customer/favorites/productors'

    def test_favorite_valid_announcement(self):
        fav_announ = {
            'email': self.productor_data['email'],
            'announcementName': self.announcement_one['name']
        }

        response = self.client.patch(
            path=self.announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')

        response = self.client.get(
            path=self.list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 1, msg='Falha na quantidade de anúncios listados')

    def test_favorite_invalid_announcement_name(self):
        fav_announ = {
            'email': self.productor_data['email'],
            'announcementName': 'invalid'
        }

        response = self.client.patch(
            path=self.announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Favorito registrado com sucesso')

        response = self.client.get(
            path=self.list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 0, msg='Falha na quantidade de anúncios listados')

    def test_favorite_announ_invalid_productor_email(self):
        fav_announ = {
            'email': 'invalid@exemplo.com',
            'announcementName': self.announcement_one['name']
        }

        response = self.client.patch(
            path=self.announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Favorito registrado com sucesso')

        response = self.client.get(
            path=self.list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 0, msg='Falha na quantidade de anúncios listados')

    def test_unfavorite_announcement(self):
        fav_announ = {
            'email': self.productor_data['email'],
            'announcementName': self.announcement_one['name']
        }

        response = self.client.patch(
            path=self.announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')

        response = self.client.patch(
            path=self.announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')
        response = self.client.get(
            path=self.list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 0, msg='Falha na quantidade de anúncios listados')

    def test_list_favorites_announcements(self):
        response = self.client.get(
            path=self.list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 0, msg='Falha na quantidade de anúncios lsitados')
    
    def test_favorite_valid_productor(self):
        fav_prod = {
            'email': self.productor_data['email']
        }

        response = self.client.patch(
            path=self.productor_fav_url,
            data=fav_prod,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')

        response = self.client.get(
            path=self.list_fav_productors_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores favoritos')
        self.assertEqual(len(response.data['idProdFav']), 1, msg='Falha na quantidade de produtores listados')

    def test_favorite_invalid_productor(self):
        invalid_fav_prod = {
            'email': 'thomas@teste.com'
        }

        response = self.client.patch(
            path=self.productor_fav_url,
            data=invalid_fav_prod,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Registrado favorito com email invalido')

        response = self.client.get(
            path=self.list_fav_productors_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores favoritos')
        self.assertEqual(len(response.data['idProdFav']), 0, msg='Falha na quantidade de produtores listados')

    def test_unfavorite_productor(self):
        fav_prod = {
            'email': self.productor_data['email'],
        }

        response = self.client.patch(
            path=self.productor_fav_url,
            format='json',
            data=fav_prod,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')

        response = self.client.patch(
            path=self.productor_fav_url,
            format='json',
            data=fav_prod,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na remoção de favorito')

        response = self.client.get(
            path=self.list_fav_productors_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores favoritos')
        self.assertEqual(len(response.data['idProdFav']), 0, msg='Falha na quantidade de produtores listados')

    def test_list_favorites_productors(self):
        response = self.client.get(
            path=self.list_fav_productors_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de produtores favoritos')
        self.assertEqual(len(response.data['idProdFav']), 0, msg='Falha na quantidade de produtores lsitados')

    def test_list_invalid_favorites_category(self):
        invalid_url = '/customer/favorites/invalid'

        response = self.client.get(
            path=invalid_url,
            format='json',
            **self.creds
        )
        self.assertEqual(response.status_code, 400, msg='Favorito válido')

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Announcement.objects.all().delete()
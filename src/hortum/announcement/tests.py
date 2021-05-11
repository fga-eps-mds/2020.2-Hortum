import os
import io

from PIL import Image

from rest_framework.test import APITestCase

from django.conf import settings

from ..productor.models import Productor
from ..customer.models import Customer
from ..users.models import User
from .models import Announcement, AnnouncementImage

from ..encode import encode_string

class AnnouncementCreateAPIViewTestCase(APITestCase):
    def create_productor(self):
        self.user_data = {
	        "username": "Mário",
            "email": "mario@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

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

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def setUp(self):
        self.create_productor()
        self.create_tokens()
        self.announcement_data = {
            "name": "Banana",
            "type_of_product": "Banana",
            "description": "vendendo banana",
            "price": 10.0,
            "localizations": [],
            "images": []
        }
        self.url_announcement = '/announcement/create'
    
    def tearDown(self):
        Announcement.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name != 'person-male.png':
                    os.remove(root + '/' + name)

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

    def test_create_announcement_with_image(self):
        photo_file = self.generate_photo_file()
        self.announcement_data['images'] += [photo_file]
        response = self.client.post(
            self.url_announcement,
            self.announcement_data,
            format='multipart',
            **self.auth_token
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Falha na criação de anúncio'
        )

        announcementImage = AnnouncementImage.objects.get(idImage__idProductor__user__email=self.user_data['email'])
        expected = AnnouncementImage.upload_image_announ(announcementImage, photo_file.name)
        self.assertEqual(response.status_code, 201, msg="Falha ao registrar anúncio")
        self.assertEqual(
            announcementImage.picture.url,
            '/images/' + expected,
            msg='Falha no link da foto'
        )

    def test_duplicate_announcement_name(self):
        other_announcement = {
            "name": "Banana",
            "type_of_product": "Banana",
            "description": "banana à venda",
            "price": 12.5,
            "localizations": [],
            "images": []
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

    def test_create_announcement_with_four_locations(self):
        self.announcement_data['localizations'] = [
            "teste 1",
            "teste 2",
            "teste 3",
            "teste 4"
        ]

        response = self.client.post(
            self.url_announcement,
            self.announcement_data,
            format='json',
            **self.auth_token
        )

        self.assertEqual(response.status_code, 400, msg='Anúncio criado com sucesso')

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

    def create_announcement(self):
        self.announcement_data = {
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50,
            "localizations": [],
            "images": []
        }

        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_data,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

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
        self.create_announcement()

        self.url_update_announ = '/announcement/update/' + self.announcement_data['name']

    def tearDown(self):
        Announcement.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name != 'person-male.png':
                    os.remove(root + '/' + name)

    def test_delete_announcement(self):
        response = self.client.delete(
            path=self.url_update_announ,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 204, msg='Falha na deleção do anúncio')
    
    def test_delete_invalid_announcement(self):
        url_delete_invalid = '/announcement/update/invalid'

        response = self.client.delete(
            path=url_delete_invalid,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 403, msg='Anúncio válido')

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
            "price": 60.15,
            "localizations": [
                "new local 1"
            ]
        }

        response = self.client.patch(
            path=self.url_update_announ,
            format='json',
            data=new_data,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração do anúncio')

    def test_update_duplicated_name_announcement(self):
        new_data = {
            "name": "Meio quilo de linguíça"
        }

        response = self.client.patch(
            path=self.url_update_announ,
            format='json',
            data=new_data,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Nome não existente no banco')

    def test_update_localizations_announcement(self):
        new_data = {
            "localizations": [
                "new local 1",
                "new local 2"
            ]
        }

        response = self.client.patch(
            path=self.url_update_announ,
            format='json',
            data=new_data,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração das localizações')
        
    def test_update_announcement_with_four_locations(self):
        new_data = {
            "localizations": [
                "teste 1",
                "teste 2",
                "teste 3",
                "teste 4"
            ]
        }

        response = self.client.patch(
            self.url_update_announ,
            new_data,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Anúncio atualizado com sucesso')

    def test_update_images_announcement(self):
        photo_file = self.generate_photo_file()
        new_data = {
            "images": [photo_file]
        }

        response = self.client.patch(
            path=self.url_update_announ,
            format='multipart',
            data=new_data,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na alteração das imagens')

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

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def create_announcement(self):
        photo_file = self.generate_photo_file()
        self.announcement_data = {
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50,
            "localizations": [
                "local 1"
            ],
            "images": [photo_file]
        }
    
        self.announcement_data_extra = {
            "name": "Meio quilo de defumado",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Defumados",
            "price": 10.15,
            "localizations": [
                "local 1",
                "local 2"
            ],
            "images": []
        }

        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement_data,
	        format='multipart',
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
        self.filter_option = '/?filter='
        self.value_option = '&value='

    def tearDown(self):
        Announcement.objects.all().delete()
        Productor.objects.all().delete()
        User.objects.all().delete()
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name != 'person-male.png':
                    os.remove(root + '/' + name)

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
        self.filter_option += 'name'
        self.value_option += 'Meio'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio com o nome inserido')
        self.assertEqual(len(response.data), 2, msg='Falha na quantidade de anúncios listados')

    def test_list_names_one_announcement(self):
        self.filter_option += 'name'
        self.value_option += 'Meio quilo de linguíça'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 1, msg='Falha na busca por anúncio')

    def test_list_containing_name_announcement(self):
        self.filter_option += 'name'
        self.value_option += 'quilo de'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 2, msg='Falha na busca por anúncio')

    def test_list_locals_multiples_annoucement(self):
        self.filter_option += 'localizations__adress'
        self.value_option += 'local 1'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio com o nome inserido')
        self.assertEqual(len(response.data), 2, msg='Falha na quantidade de anúncios listados')

    def test_list_local_one_announcement(self):
        self.filter_option += 'localizations__adress'
        self.value_option += 'local 2'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 1, msg='Falha na busca por anúncio')

    def test_list_containing_local_announcement(self):
        self.filter_option += 'localizations__adress'
        self.value_option += 'local'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Nenhum anúncio encontrado')
        self.assertEqual(len(response.data), 2, msg='Falha na busca por anúncio')

    def test_list_invalid_query_params_announcement(self):
        self.filter_option += 'name'
        self.url_list_announ += self.filter_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 404, msg='Opção válida para busca')

    def test_list_tree_query_params_announcement(self):
        self.filter_option += 'name'
        self.value_option += 'invalid'
        third_option = '&third=invalid'
        self.url_list_announ += self.filter_option + self.value_option + third_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 404, msg='Quantidade válida para busca')

    def test_list_invalid_filter_announcement(self):
        self.filter_option += 'invalid'
        self.value_option += 'invalid'
        self.url_list_announ += self.filter_option + self.value_option

        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Filtro válido para busca')

    def test_announcement_order(self):
        response = self.client.get(
            path=self.url_list_announ,
            **self.creds
        )

        most_recent = response.data[0]
        self.assertEqual(most_recent['description'], 'Defumados', msg='Ordem de listagem incorreta')

class AnnouncementRetrieveAPIViewTestCase(APITestCase):
    def create_productor(self):
        self.productor_data = {
	        "username": "Mário",
            "email": "mario@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': self.productor_data},
	        format='json'
	    )

        User.objects.filter(email=self.productor_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')

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

        response = self.client.post(
            url_signup,
	        {'user': self.customer_data},
	        format='json'
	    )

        User.objects.filter(email=self.customer_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')

    def create_announcements(self):
        self.announcement_one = {
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50,
            "localizations": [],
            "images": []
        }
    
        self.announcement_two = {
            "name": "Meio quilo de defumado",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Defumados",
            "price": 10.15,
            "inventory": False,
            "localizations": [],
            "images": []
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

        self.url_retrieve = '/announcement/retrieve/'

    def tearDown(self):
        Productor.objects.all().delete()
        Customer.objects.all().delete()
        Announcement.objects.all().delete()

    def test_retrieve_productor(self):
        email_query = 'mario@teste.com'
        url_retrieve_productor = self.url_retrieve + encode_string(email_query)

        response = self.client.get(
            url_retrieve_productor,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na obtenção de produtor específico')
        self.assertEqual(len(response.data), 2, msg='Dados de produtor estão incoerentes')

    def test_invalid_email(self):
        email_query = 'luigi@teste.com'
        url_retrieve_productor = self.url_retrieve + encode_string(email_query)

        response = self.client.get(
            url_retrieve_productor,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Retornando produtor com email inválido')

    def test_retrieve_productor_from_customer(self):
        self.create_tokens(self.customer_data)

        email_query = 'mario@teste.com'
        url_retrieve_productor = self.url_retrieve + encode_string(email_query)

        response = self.client.get(
            url_retrieve_productor,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na obtenção de produtor específico')
        self.assertEqual(len(response.data), 1, msg='Dados de produtor estão incoerentes')
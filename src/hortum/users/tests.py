import os
import io

from PIL import Image
from unittest import mock

from rest_framework.test import APITestCase

from django.conf import settings
from django.db import DataError

from ..customer.models import Customer
from ..productor.models import Productor
from ..announcement.models import Announcement
from ..validators import qs_exists, qs_filter

from .models import User
from .forms import CustomPasswordForm

class GlobalValidatorTestCase(APITestCase):
    '''
    Validação retirada do `ValidatorTests`
    do Django Rest e adaptada para o projeto
    '''
    def test_qs_exists_handles_type_error(self):
        class TypeErrorQueryset:
            def exists(self):
                raise TypeError
        self.assertFalse(qs_exists(TypeErrorQueryset()))

    def test_qs_exists_handles_value_error(self):
        class ValueErrorQueryset:
            def exists(self):
                raise ValueError
        self.assertFalse(qs_exists(ValueErrorQueryset()))

    def test_qs_exists_handles_data_error(self):
        class DataErrorQueryset:
            def exists(self):
                raise DataError
        self.assertFalse(qs_exists(DataErrorQueryset()))

    def test_qs_filter_handles_type_error(self):
        class TypeErrorQueryset:
            def filter(self, **kwargs):
                raise TypeError

            def none(self):
                return None
        self.assertEqual(qs_filter(TypeErrorQueryset()), None)

    def test_qs_filter_handles_value_error(self):
        class ValueErrorQueryset:
            def filter(self, **kwargs):
                raise ValueError

            def none(self):
                return None
        self.assertEqual(qs_filter(ValueErrorQueryset()), None)

    def test_qs_filter_handles_data_error(self):
        class DataErrorQueryset:
            def filter(self, **kwargs):
                raise DataError
                
            def none(self):
                return None
        self.assertEqual(qs_filter(DataErrorQueryset()), None)

class CustomPasswordFormTestCase(APITestCase):
    '''
    Validação retirada do `SetPasswordFormTest`
    do Django e adaptada para o projeto.
    '''
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste",
            "phone_number": "62123456787"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.user = User.objects.get(email=self.user_data['email'])
        User.objects.filter(email=self.user_data['email']).update(is_verified=True)

    def setUp(self):
        self.create_user()

    def test_password_verification(self):
        data = {
            'new_password1': '12345',
            'new_password2': '123'
        }
        form = CustomPasswordForm(self.user, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['new_password2'].errors, [str(form.error_messages['password_mismatch'])])

    @mock.patch('django.contrib.auth.password_validation.password_changed')
    def test_success_change_password(self, password_changed):
        data = {
            'new_password1': '12345',
            'new_password2': '12345'
        }
        form = CustomPasswordForm(self.user, data)
        self.assertTrue(form.is_valid())
        form.save(commit=False)
        self.assertEqual(password_changed.call_count, 0)
        form.save()
        self.assertEqual(password_changed.call_count, 1)

class UserCreateAPIViewTestCase(APITestCase):
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def setUp(self):
        self.url_verified_page = '/users/verify/'
        self.url_login = '/signup/customer/'

    def tearDown(self):
        User.objects.all().delete()
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name != 'person-male.png':
                    os.remove(root + '/' + name)

    def test_create_valid_user(self):
        user_data = {
            "username": "João",
            "email": "joao@email.com",
            "phone_number": "61121456789",
            "password": "teste"
        }

        response = self.client.post(
            self.url_login,
            {'user': user_data},
            format='json'
        )

        User.objects.filter(email=user_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')
        # self.assertTemplateUsed(response, 'hortum/user_verify_page.html')

    def test_create_valid_user_with_image(self):
        photo_file = self.generate_photo_file()
        user_data = {
            "user.username": "Cleber",
            "user.email": "cleber@email.com",
            "user.phone_number": "61121456789",
            "user.password": "teste",
            "user.profile_picture": photo_file
        }

        response = self.client.post(
            self.url_login,
            user_data,
            format='multipart'
        )

        User.objects.filter(email=user_data['user.email']).update(is_verified=True)

        expected = User.upload_image(User.objects.get(username=user_data['user.username']), photo_file.name)
        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')
        self.assertEqual(response.data['user']['profile_picture'], 'http://testserver/images/' + expected, msg='Falha no link da foto')

    def test_is_verified_render_page(self):
        self.url_verified_page += 'am9hb0BlbWFpbC5jb20='
        user_data = {
            "username": "João",
            "email": "joao@email.com",
            "phone_number": "61121456789",
            "password": "teste"
        }

        response = self.client.post(
            self.url_login,
            {'user': user_data},
            format='json'
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')

        response = self.client.get(self.url_verified_page)
        self.assertTemplateUsed(response, 'hortum/user_verify_page.html')

    def test_is_already_verified_render_page(self):
        self.url_verified_page += 'am9hb0BlbWFpbC5jb20='
        user_data = {
            "username": "João",
            "email": "joao@email.com",
            "phone_number": "61121456789",
            "password": "teste"
        }

        response = self.client.post(
            self.url_login,
            {'user': user_data},
            format='json'
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação de usuário')
        User.objects.filter(email=user_data['email']).update(is_verified=True)

        response = self.client.get(self.url_verified_page)
        self.assertTemplateUsed(response, 'hortum/user_already_verified_page.html')

    def test_create_invalid_user(self):
        user_data = {
            "username": "João",
            "password": "teste"
        }

        response = self.client.post(
            self.url_login,
            {'user': user_data},
            format='json'
        )

        self.assertEqual(response.status_code, 400, msg='Usuário criado com sucesso')

    def test_create_duplicated_phone_number_user(self):
        self.test_create_valid_user()
        user_data = {
            "username": "João",
            "email": "joao@email.com",
            "phone_number": "11123456789",
            "password": "teste"
        }

        response = self.client.post(
            self.url_login,
            {'user': user_data},
            format='json'
        )

        User.objects.filter(email=user_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 400, msg='Falha na criação de usuário')

class UserTokenObtainAPIViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste",
            "phone_number": "62123456787"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        User.objects.filter(email=self.user_data['email']).update(is_verified=True)

    def setUp(self):
        self.create_user()
        self.url_login = '/login/'
        self.url_test_token = '/api/test_token/'

    def tearDown(self):
        User.objects.all().delete()

    def test_user_login(self):
        user_credentials = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha no login de usuário'
        )

        self.auth_token = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def test_wrong_credentials_login(self):
        wrong_credentials = {
            'email': 'luis@teste',
            'password': 'luis'
        }

        response = self.client.post(
            self.url_login,
            wrong_credentials,
            format='json'
        )

        self.assertEqual(response.status_code, 401, msg='Login com credenciais corretas')

    def test_token_validator(self):
        self.test_user_login()

        response = self.client.get(
            self.url_test_token,
            format='json',
            **self.auth_token
        )
        
        self.assertEqual(response.status_code, 200, msg='Token inválido')

    def test_invalid_token_validator(self):
        self.test_user_login()
        
        invalid_token = {'HTTP_AUTHORIZATION': 'Bearer invalid'}
        
        response = self.client.get(
            self.url_test_token,
            format='json',
            **invalid_token
        )

        self.assertEqual(response.status_code, 401, msg='Token válido')
        self.assertEqual(response.json()['detail'], 'Given token not valid for any token type', msg='Token válido')

class UpdateUserViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
            "phone_number": "61133456789",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        User.objects.filter(email=self.user_data['email']).update(is_verified=True)
    
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
        self.url_update_user = '/users/update'

    def test_change_existent_email(self):
        other_user_data = {
            'username': 'Marcos Segundo',
            'email': 'marcos@productor.com',
            'password': 'teste dois',
            'phone_number': "41123456787"
        }
        
        user_username_email = {
	        "username": self.user_data['email'],
            "email": "marcos@productor.com"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
            {'user': other_user_data},
            format='json'
        )

        User.objects.filter(email=other_user_data['email']).update(is_verified=True)

        response = self.client.patch(
            path=self.url_update_user,
            data=user_username_email,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Email nao existente')

    def test_update_user(self):
        user_username_email = {
	        "username": "Luis2",
            "email": "luis2@productor.com"
        }

        response = self.client.patch(
            path=self.url_update_user,
            data=user_username_email,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 200, msg='Usuario nao atualizado')
    
    def test_update_valid_phone_number_user(self):
        new_information = {
            "phone_number": "62887654321"
        }

        response = self.client.patch(
            path=self.url_update_user,
            data=new_information,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Número de celuar não existente')

    def test_update_duplicate_phone_number_user(self):
        new_information = {
            "phone_number": "61133456789"
        }

        response = self.client.patch(
            path=self.url_update_user,
            data=new_information,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Número de celuar não existente')

    def test_empty_update_user(self):
        response = self.client.patch(
            path=self.url_update_user,
            data={},
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Campos nao vazios')
    
    def test_user_login_old_email(self):
        self.test_update_user()
        user_credentials = {
            'email': "luis@productor.com",
            'password': self.user_data['password']
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Login com credenciais incorretas'
        )
        
    def test_user_login_new_email(self):
        self.test_update_user()
        user_credentials = {
            'email': "luis2@productor.com",
            'password': self.user_data['password'],
        }
        
        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha no login de usuário'
        )

    def tearDown(self):
        Customer.objects.all().delete()
        User.objects.all().delete()

class ChangePasswordViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste",
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        User.objects.filter(email=self.user_data['email']).update(is_verified=True)
    
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
        self.url_change_password = '/users/change-password'

    def test_wrong_old_password(self):
        user_password = {
	        "old_password": "asdsd",
            "new_password": "gfdfgdgffg"
        }

        response = self.client.patch(
            path=self.url_change_password,
            data=user_password,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Senha correta inserida')

    def test_change_password(self):
        user_password = {
	        "old_password": "teste",
            "new_password": "nova senha"
        }

        response = self.client.patch(
            path=self.url_change_password,
            data=user_password,
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 200, msg='Senha nao alterada')
    
    def test_user_login_old_password(self):
        self.test_change_password()
        user_credentials = {
            'email': self.user_data['email'],
            'password': "teste"
        }

        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            401,
            msg='Login com credenciais incorretas'
        )
        
    def test_user_login_new_password(self):
        self.test_change_password()
        user_credentials = {
            'email': self.user_data['email'],
            'password': "nova senha",
        }
        
        response = self.client.post(
            self.url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha no login de usuário'
        )

    def test_empty_password_fields(self):
        response = self.client.patch(
            path=self.url_change_password,
            data={},
            format='json',
            **self.creds
        )
        
        self.assertEqual(response.status_code, 400, msg='Campos nao vazios')
        
    def tearDown(self):
        Customer.objects.all().delete()
        User.objects.all().delete()

class DeleteUserAPIViewTestCase(APITestCase):
    def create_customer(self):
        self.customer_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste",
            "phone_number": "61123456757"
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.customer_data},
	        format='json'
	    )

        User.objects.filter(email=self.customer_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Erro na criação do customer')

    def create_productor(self):
        self.productor_data = {
	        "username": "João",
            "email": "joao@teste.com",
	        "password": "teste",
            "phone_number": "61123416787"
        }

        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': self.productor_data},
	        format='json'
	    )

        User.objects.filter(email=self.productor_data['email']).update(is_verified=True)

        self.assertEqual(response.status_code, 201, msg='Erro na criação do productor')

    def create_announcements(self):
        self.announcement = {
            "name": "Meio quilo de linguíça",
            "type_of_product": "Linguiça artesanal e defumados",
            "description": "Linquiça",
            "price": 35.50,
            "images": [],
            "localizations": []
        }
    
        url_create_announ = '/announcement/create'

        response = self.client.post(
            path=url_create_announ,
	        data=self.announcement,
	        format='json',
	        **self.creds
        )

        self.assertEqual(response.status_code, 201, msg='Falha na criação do anúncio')

    def favorite_announcement(self):
        fav_announ = {
            'email': self.productor_data['email'],
            'announcementName': self.announcement['name']
        }

        announcement_fav_url = '/customer/fav-announcement'

        response = self.client.patch(
            path=announcement_fav_url,
            format='json',
            data=fav_announ,
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha no registro do favorito')

    def create_tokens(self, user_data):
        user_cred = {'email': user_data['email'], 'password': user_data['password']}

        url_token = '/login/'

        response = self.client.post(
            url_token,
	        user_cred,
	        format='json'
        )

        self.creds = {'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']}

    def setUp(self):
        self.create_customer()
        self.create_productor()
        self.create_tokens(self.productor_data)
        self.create_announcements()
        self.create_tokens(self.customer_data)
        self.favorite_announcement()

        self.delete_user_url = '/users/delete'

    def tearDown(self):
        Customer.objects.all().delete()
        Productor.objects.all().delete()
        Announcement.objects.all().delete()

    def test_delete_with_invalid_password_user(self):
        delete_info = {
            'password': 'invalid'
        }

        response = self.client.delete(
            path=self.delete_user_url,
            format='json',
            data=delete_info,
            **self.creds
        )

        self.assertEqual(response.status_code, 400, msg='Deleção correta do user')

    def test_delete_valid_customer(self):
        delete_info = {
            'password': self.customer_data['password']
        }

        response = self.client.delete(
            path=self.delete_user_url,
            format='json',
            data=delete_info,
            **self.creds
        )

        self.assertEqual(response.status_code, 204, msg='Falha na deleção do user')

    def test_delete_valid_productor(self):
        self.create_tokens(self.productor_data)
        delete_info = {
            'password': self.productor_data['password']
        }

        response = self.client.delete(
            path=self.delete_user_url,
            format='json',
            data=delete_info,
            **self.creds
        )

        self.assertEqual(response.status_code, 204, msg='Falha na deleção do user')

        self.create_tokens(self.customer_data)
        list_fav_announcements_url = '/customer/favorites/announcements'
        response = self.client.get(
            path=list_fav_announcements_url,
            format='json',
            **self.creds
        )

        self.assertEqual(response.status_code, 200, msg='Falha na listagem de anúncios favoritos')
        self.assertEqual(len(response.data['idAnunFav']), 0, msg='Falha na quantidade de anúncios listados')

class VerifyAccountViewTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste",
            "phone_number": "61121456789"
        }

        url_signup = '/signup/customer/'

        self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )
    
    def user_login(self):
        user_cred = {'email': self.user_data['email'], 'password': self.user_data['password']}

        url_login = '/login/'

        self.login_response = self.client.post(
            url_login,
	        user_cred,
	        format='json'
        )

    def setUp(self):
        self.create_user()

    def test_user_not_verified(self):
        self.user_login()
        self.assertEqual(self.login_response.status_code, 403, msg='Usuário logou sem ser verificado')

    def tearDown(self):
        Customer.objects.all().delete()
        User.objects.all().delete()
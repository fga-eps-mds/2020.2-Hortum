from rest_framework.test import APITestCase

from .models import Productor

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

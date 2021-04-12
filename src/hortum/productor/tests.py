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
            'password': 'teste dois'
        }

        response = self.client.post(
            self.url_signup,
            {'user': new_user},
            format='json'
        )

        self.assertEqual(response.status_code, 400, msg='Email inexistente')
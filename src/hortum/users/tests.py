from rest_framework.test import APITestCase

from ..customer.models import Customer

class UserAPIViewsTestCase(APITestCase):
    def create_user(self):
        self.user_data = {
	        "username": "Luís",
            "email": "luis@teste.com",
	        "password": "teste"
        }

        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

    def setUp(self):
        self.create_user()

    def tearDown(self):
        Customer.objects.all().delete()

    def test_user_login(self):
        user_credentials = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        url_login = '/login/'

        response = self.client.post(
            url_login,
	        user_credentials,
	        format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Falha no login de usuário'
        )

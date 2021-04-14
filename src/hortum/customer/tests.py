from rest_framework.test import APITestCase

from .models import Customer

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
from rest_framework.test import APITestCase

from .models import Customer

class CustomerRegisterAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Pedro',
            'email': 'pedro@customer.com',
            'password': 'teste'
        }

    def tearDown(self):
        Customer.objects.all().delete()

    def test_customer_register(self):
        url_signup = '/signup/customer/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.assertEqual(
            response.status_code,
            201,
            msg='Falha no registro de comprador'
        )
        
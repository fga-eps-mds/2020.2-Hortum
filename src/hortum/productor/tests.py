from rest_framework.test import APITestCase

from .models import Productor

class ProductorAPIViewsTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'Marcos',
            'email': 'marcos@productor.com',
            'password': 'teste'
        }

    def tearDown(self):
        Productor.objects.all().delete()

    def test_productor_register(self):
        url_signup = '/signup/productor/'

        response = self.client.post(
            url_signup,
	        {'user': self.user_data},
	        format='json'
	    )

        self.assertEqual(
            response.status_code,
            201,
            msg='Falha no registro de produtor'
        )

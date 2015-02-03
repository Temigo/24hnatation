from rest_framework.test import APITestCase

from nat24h_base.models import User

class GroupPermsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='bob')

    def test_add_group(self):
        data = {'name': 'BR', 'type': 'binet'}

        self.client.force_authenticate(user=self.user)
        response = self.client.post('/group/', data)
        self.assertEqual(response.status_code, 201)

from rest_framework.test import APITestCase
from django.contrib.auth.models import Permission

from nat24h_base.models import User


class GroupPermsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='bob')
        perm = Permission.objects.get(codename='add_group', content_type__app_label='nat24h_base')
        self.user.user_permissions.add(perm)
        self.user.save()
        self.user2 = User.objects.create(username='alice')

    def test_add_group(self):
        data = {'name': 'BR', 'type': 'binet'}

        self.client.force_authenticate(user=self.user)
        response = self.client.post('/group/', data)
        self.assertEqual(response.status_code, 201)

        self.client.force_authenticate(user=self.user2)
        response = self.client.post('/group/', data)
        self.assertEqual(response.status_code, 403)

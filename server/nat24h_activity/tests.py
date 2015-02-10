from django.utils import timezone
from rest_framework.test import APITestCase

from nat24h_base.models import User
from nat24h_activity.models import Activity, Team

class TeamPermsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='bob')
        self.user2 = User.objects.create(email='alice')

        self.activity = Activity.objects.create(name='Test', start=timezone.now(), end=timezone.now())

    def test_add_team(self):
        data = {'name': 'BR', 'admin': self.user.id, 'activity': self.activity.pk}

        self.client.force_authenticate(user=self.user)
        response = self.client.post('/team/', data)
        self.assertEqual(response.status_code, 201)

    def test_edit_team(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Faerix', 'admin': self.user.id, 'activity': self.activity.pk}

        Team.objects.create(admin=self.user, name='BR', activity=self.activity)
        response = self.client.put('/team/1/', data)
        self.assertEqual(response.status_code, 200)

        Team.objects.create(admin=self.user2, name='BR', activity=self.activity)
        response = self.client.put('/team/2/', data)
        self.assertEqual(response.status_code, 403)

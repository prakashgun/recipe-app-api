from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@example.com', password='test')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='test@example.com', password='test',
                                                         name='test user full name')

    def test_users_listed(self):
        """ Test users are listed in the user list page in django admin """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/{id}
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

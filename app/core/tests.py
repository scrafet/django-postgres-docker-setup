from django.test import TestCase, Client
from django.urls import reverse
from .models import Item
from django.contrib.auth.models import User
from django.test import override_settings

@override_settings(SECURE_SSL_REDIRECT=False)
class ItemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.item = Item.objects.create(name='Test Item', description='Test Description', price=10.00)

    def test_login_required(self):
        response = self.client.get(reverse('item_list'))
        self.assertNotEqual(response.status_code, 200)
        # It will redirect to login page.
        # Since we are using standard redirects, it should be 302.
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

    def test_item_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

    def test_item_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('item_add'), {
            'name': 'New Item',
            'description': 'New Description',
            'price': 20.00
        })
        self.assertEqual(response.status_code, 302) # Redirects to list
        self.assertTrue(Item.objects.filter(name='New Item').exists())

    def test_item_update_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('item_edit', args=[self.item.pk]), {
            'name': 'Updated Item',
            'description': 'Updated Description',
            'price': 15.00
        })
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_item_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('item_delete', args=[self.item.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())

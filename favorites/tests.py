from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gifts.models import Gift
from favorites.models import Favorite


class FavoriteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.gift = Gift.objects.create(name="Test Gift", description="Test", price=10.00)
        self.add_url = reverse('add_to_favorites', args=[self.gift.id])
        self.remove_url = reverse('remove_from_favorites', args=[self.gift.id])
        self.list_url = reverse('favorite_list')

    def test_add_to_favorites_requires_login(self):
        response = self.client.get(self.add_url)
        self.assertRedirects(response, f'/accounts/login/?next={self.add_url}')

    def test_add_to_favorites_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.add_url)
        self.assertRedirects(response, reverse('gift_detail', args=[self.gift.id]))

        favorite_exists = Favorite.objects.filter(user=self.user, gift=self.gift).exists()
        self.assertTrue(favorite_exists)

    def test_remove_from_favorites(self):
        Favorite.objects.create(user=self.user, gift=self.gift)
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.remove_url)
        self.assertRedirects(response, reverse('gift_detail', args=[self.gift.id]))

        favorite_exists = Favorite.objects.filter(user=self.user, gift=self.gift).exists()
        self.assertFalse(favorite_exists)

    def test_favorite_list_only_shows_user_favorites(self):
        another_user = User.objects.create_user(username='otheruser', password='otherpass')
        other_gift = Gift.objects.create(name="Other Gift", description="Other", price=20.00)
        Favorite.objects.create(user=self.user, gift=self.gift)
        Favorite.objects.create(user=another_user, gift=other_gift)

        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/favorite_list.html')
        favorites = response.context['favorites']
        self.assertEqual(favorites.count(), 1)
        self.assertEqual(favorites.first().gift, self.gift)

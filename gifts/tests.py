from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gifts.models import Gift, Category, Occasion, Size


class GiftViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser('admin', 'admin@test.com', 'password123')
        self.user = User.objects.create_user('regular', 'user@test.com', 'password123')
        self.category = Category.objects.create(name='test-cat', friendly_name='Test Category')
        self.occasion = Occasion.objects.create(name='birthday', friendly_name='Birthday')
        self.size = Size.objects.create(name='Medium')

        self.gift = Gift.objects.create(
            name="Test Gift",
            description="A test gift",
            has_sizes=True,
            occasion=self.occasion,
            category=self.category,
            size=self.size,
            quantity=5,
            price=19.99,
            image='test.jpg'
        )

    def test_all_gifts_view(self):
        response = self.client.get(reverse('gifts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gifts/gift_list.html')
        self.assertContains(response, self.gift.name)

    def test_gift_detail_view(self):
        response = self.client.get(reverse('gift_detail', args=[self.gift.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gifts/gift_detail.html')
        self.assertContains(response, self.gift.description)

    def test_add_gift_requires_superuser(self):
        self.client.login(username='regular', password='password123')
        response = self.client.get(reverse('add_gift'))
        self.assertRedirects(response, reverse('home'))

    def test_add_gift_superuser_access(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('add_gift'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gifts/add_gift.html')

    def test_add_gift_submission(self):
        self.client.login(username='admin', password='password123')
        response = self.client.post(reverse('add_gift'), {
            'name': 'New Gift',
            'description': 'Something nice',
            'has_sizes': False,
            'occasion': self.occasion.id,
            'category': self.category.id,
            'size': self.size.id,
            'quantity': 10,
            'price': 25.00,
        }, follow=True)
        self.assertContains(response, 'Successfully added gift!')
        self.assertTrue(Gift.objects.filter(name='New Gift').exists())

    def test_edit_gift_superuser_only(self):
        self.client.login(username='regular', password='password123')
        response = self.client.get(reverse('edit_gift', args=[self.gift.id]))
        self.assertRedirects(response, reverse('home'))

    def test_edit_gift_form_display_and_submission(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('edit_gift', args=[self.gift.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gifts/edit_gift.html')

        response = self.client.post(reverse('edit_gift', args=[self.gift.id]), {
            'name': 'Updated Gift',
            'description': 'Updated description',
            'has_sizes': True,
            'occasion': self.occasion.id,
            'category': self.category.id,
            'size': self.size.id,
            'quantity': 10,
            'price': 30.00,
        }, follow=True)
        self.assertContains(response, 'Successfully updated gift!')
        self.gift.refresh_from_db()
        self.assertEqual(self.gift.name, 'Updated Gift')

    def test_delete_gift_superuser_only(self):
        self.client.login(username='regular', password='password123')
        response = self.client.get(reverse('delete_gift', args=[self.gift.id]))
        self.assertRedirects(response, reverse('home'))

    def test_delete_gift_superuser(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('delete_gift', args=[self.gift.id]), follow=True)
        self.assertContains(response, 'Gift deleted!')
        self.assertFalse(Gift.objects.filter(id=self.gift.id).exists())

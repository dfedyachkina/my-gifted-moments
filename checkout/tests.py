from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

from gifts.models import Gift
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile


class CheckoutViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', 
                                            password='testpass')
        self.profile = UserProfile.objects.create(user=self.user)
        self.gift = Gift.objects.create(name="Test Gift", price=10.00)

        session = self.client.session
        session['bag'] = {
            str(self.gift.id): 2
        }
        session.save()

    def test_checkout_page_renders(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_form_valid_submission_creates_order(self):
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test Town',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': '',
        }
        response = self.client.post(reverse('checkout'), data=form_data)
        self.assertEqual(response.status_code, 302)
        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Test User')
        self.assertEqual(order.email, 'test@example.com')
        self.assertEqual(order.order_total, 20.00)
        self.assertEqual(OrderLineItem.objects.count(), 1)

    def test_checkout_success_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            postcode='12345',
            town_or_city='Test Town',
            street_address1='123 Test St',
            street_address2='',
            county='',
            order_total=20,
            delivery_cost=0,
            grand_total=20,
        )
        order_number = order.order_number
        response = self.client.get(reverse('checkout_success', args=[order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        updated_order = Order.objects.get(order_number=order_number)
        self.assertEqual(updated_order.user_profile, self.profile)

from django.test import TestCase, Client
from django.urls import reverse
from gifts.models import Gift


class BagViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.gift = Gift.objects.create(name="Test Gift", price=10.00)

    def test_view_bag(self):
        response = self.client.get(reverse('bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_without_size(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.gift.id]),
            data={'quantity': 2, 'redirect_url': reverse('bag')}
        )
        self.assertRedirects(response, reverse('bag'))
        session = self.client.session
        self.assertIn(str(self.gift.id), session['bag'])
        self.assertEqual(session['bag'][str(self.gift.id)], 2)

    def test_add_to_bag_with_size(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.gift.id]),
            data={
                'quantity': 1,
                'redirect_url': reverse('bag'),
                'gift_size': 'M'
            }
        )
        self.assertRedirects(response, reverse('bag'))
        session = self.client.session
        self.assertIn(str(self.gift.id), session['bag'])
        self.assertEqual(session['bag'][str(self.gift.id)]
        ['items_by_size']['M'], 1)

    def test_adjust_bag_quantity_without_size(self):
        session = self.client.session
        session['bag'] = {str(self.gift.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.gift.id]),
            data={'quantity': 5}
        )
        self.assertRedirects(response, reverse('bag'))
        session = self.client.session
        self.assertEqual(session['bag'][str(self.gift.id)], 5)

    def test_adjust_bag_quantity_with_size(self):
        session = self.client.session
        session['bag'] = {str(self.gift.id): {'items_by_size': {'L': 2}}}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.gift.id]),
            data={'quantity': 4, 'gift_size': 'L'}
        )
        self.assertRedirects(response, reverse('bag'))
        session = self.client.session
        self.assertEqual(session['bag'][str(self.gift.id)]
        ['items_by_size']['L'], 4)

    def test_remove_from_bag_without_size(self):
        session = self.client.session
        session['bag'] = {str(self.gift.id): 1}
        session.save()

        response = self.client.post(reverse('remove_from_bag', args=[self.gift.id]))
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.gift.id), session['bag'])

    def test_remove_from_bag_with_size(self):
        session = self.client.session
        session['bag'] = {str(self.gift.id): {'items_by_size': {'S': 1}}}
        session.save()

        response = self.client.post(
            reverse('remove_from_bag', args=[self.gift.id]),
            data={'gift_size': 'S'}
        )
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.gift.id), session['bag'])

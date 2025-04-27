from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order
from .models import UserProfile
from profiles.forms import UserProfileForm
from django_countries.fields import Country


class UserProfileTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.profile = self.user.userprofile
        self.client.login(username='testuser', password='testpass123')
        self.url = reverse('profile')

    # --- Model Tests ---
    def test_profile_creation_on_user_creation(self):
        """ Test that a profile is created automatically when a user is created """
        user = User.objects.create_user(username='newuser', password='newpassword123')
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.user.username, 'newuser')
        self.assertEqual(profile.default_phone_number, None)

    # --- Form Tests ---
    def test_userprofile_form_valid(self):
        """ Test valid form submission """
        data = {
            'default_phone_number': '123456789',
            'default_postcode': 'AB12CD',
            'default_town_or_city': 'TestTown',
            'default_street_address1': '123 Test Street',
            'default_street_address2': '',
            'default_county': 'TestCounty',
            'default_country': 'GB',
        }
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_profile_view_post_invalid(self):
        """ Test that profile form shows errors with invalid POST data """
        invalid_data = {
            'default_phone_number': 'invalid-phone',
            'default_postcode': '', 
        }
        response = self.client.post(reverse('profile'), invalid_data)
        self.assertFormError(response, 'form', 'default_phone_number', 'Enter a valid phone number.')
        self.assertFormError(response, 'form', 'default_postcode', 'This field is required.')
        self.assertEqual(UserProfile.objects.count(), 1)


    def test_profile_view_renders_correct_template(self):
        """ Test that the profile page renders with correct template and data """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Profile')

    def test_profile_view_post_valid(self):
        """ Test that profile form updates with valid POST data """
        data = {
            'default_phone_number': '123456789',
            'default_postcode': 'AB12CD',
            'default_town_or_city': 'TestTown',
            'default_street_address1': '123 Test Street',
            'default_street_address2': '',
            'default_county': 'TestCounty',
            'default_country': 'GB',
        }
        response = self.client.post(self.url, data, follow=True)
        self.assertContains(response, 'Profile updated successfully')

        # Refresh from DB and check data
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '123456789')
        self.assertEqual(self.profile.default_country.code, 'GB')

    def test_profile_view_post_invalid(self):
        """ Test that profile form shows errors with invalid POST data """
        data = {'default_phone_number': '', 'default_postcode': ''}  # missing required fields
        response = self.client.post(self.url, data, follow=True)
        self.assertContains(response, 'Update failed')

    # Test order history (if applicable, or remove if not needed)
    def test_order_history_view(self):
        order_url = reverse('order_history', args=['order123'])
        response = self.client.get(order_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, 'order123')

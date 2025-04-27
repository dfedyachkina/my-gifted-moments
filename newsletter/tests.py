from django.test import TestCase, Client
from django.urls import reverse
from newsletter.models import Newsletter


class NewsletterViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('newsletter')

    def test_newsletter_page_loads(self):
        """ Test GET request renders the newsletter page with the form """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter.html')
        self.assertContains(response, '<form')

    def test_newsletter_valid_submission(self):
        """ Test valid form submission adds email to database """
        response = self.client.post(self.url, {'email': 'test@example.com'},
        follow=True)
        self.assertContains(response, 'Thank you for subscription!')
        self.assertEqual(Newsletter.objects.count(), 1)
        self.assertEqual(Newsletter.objects.first().email, 'test@example.com')

    def test_newsletter_invalid_submission(self):
        """ Test invalid form submission does not create object """
        response = self.client.post(self.url, {'email': 'invalid-email'}, follow=True)
        self.assertNotContains(response, 'Thank you for subscription!')
        self.assertEqual(Newsletter.objects.count(), 0)

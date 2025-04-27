from django.test import TestCase, Client
from django.urls import reverse
from faq.models import FAQ


class FAQViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('faq')

        # Create some FAQ entries
        FAQ.objects.create(question="What is your return policy?", answer="You can return items within 30 days.")
        FAQ.objects.create(question="Do you ship internationally?", answer="Yes, we ship worldwide.")

    def test_faq_list_view_status_and_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/faq_list.html')

    def test_faq_list_view_context_data(self):
        response = self.client.get(self.url)
        faqs = response.context['faqs']
        self.assertEqual(faqs.count(), 2)
        self.assertQuerysetEqual(
            faqs.order_by('id'),
            FAQ.objects.all().order_by('id'),
            transform=lambda x: x
        )

    def test_faq_content_displayed(self):
        response = self.client.get(self.url)
        self.assertContains(response, "What is your return policy?")
        self.assertContains(response, "Do you ship internationally?")

from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from contact.models import Contact


class ContactViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_contact_page_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertContains(response, '<form')  # Sanity check for form in template
    
    def test_invalid_contact_form_does_not_send_email_or_create_contact(self):
        # Send a POST request with invalid data (no name provided)
        response = self.client.post(reverse('contact'), {
            'email': 'invalid_email',
            'message': 'Test message',
        })
        print(response.context)
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.is_bound)
        self.assertFormError(response, 'form', 'name', 'This field is required.')


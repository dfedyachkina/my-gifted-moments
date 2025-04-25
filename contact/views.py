from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email to admin
            subject = f"New Contact Message from {contact.name}"
            message = (
                f"You have received a new message via the contact form:\n\n"
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Message:\n{contact.message}\n"
                f"Sent on: {contact.date_sent.strftime('%Y-%m-%d %H:%M')}"
            )
            admin_email = 'my.gifted.moments123@gmail.com'
            if admin_email:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])  # noqa

            # User feedback
            messages.success(request, 'Thank you for your message! We will get back to you soon.')  # noqa
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

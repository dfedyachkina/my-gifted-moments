from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()

            # User feedback
            messages.success(request, 'Thank you for subscription!')
            return redirect('newsletter')
    else:
        form = NewsletterForm()

    return render(request, 'newsletter/newsletter.html', {'form': form})

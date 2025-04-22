from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all().order_by('id')
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

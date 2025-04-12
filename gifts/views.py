from django.views.generic import ListView, DetailView
from .models import Gift


class Gifts(ListView):
    model = Gift
    template_name = "gifts/gift_list.html"
    context_object_name = "gifts"


class GiftDetailView(DetailView):
    model = Gift
    template_name = "gifts/gift_detail.html"
    context_object_name = "gift"

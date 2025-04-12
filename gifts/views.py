from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Gift

def all_gifts(request):
    """ A view to show all gifts, including sorting and search queries """
    gifts = Gift.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('gifts'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        gifts = gifts.filter(queries)

    context = {
        'gifts': gifts,
        'search_term': query,
    }

    return render(request, 'gifts/gift_list.html', context)


def gift_detail(request, gift_id):
    """ A view to show individual gift details """
    gift = get_object_or_404(Gift, pk=gift_id)

    context = {
        'gift': gift,
    }
    return render(request, 'gifts/gift_detail.html', context)

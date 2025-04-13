from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Gift, Category, Occasion

def all_gifts(request):
    """ A view to show all gifts, including sorting and search queries """
    gifts = Gift.objects.all()
    query = None
    current_categories = None
    current_occasions = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            gifts = gifts.annotate(lower_name=Lower('name'))
            sortkey = 'lower_name'
        elif sortkey == 'category':
            sortkey = 'category__name'
        elif sortkey == 'price':
            sortkey = 'price'

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        gifts = gifts.order_by(sortkey)



    if 'occasion' in request.GET:
        occasion_names = request.GET['occasion'].split(',')
        gifts = gifts.filter(occasion__name__in=occasion_names)
        current_occasions = Occasion.objects.filter(name__in=occasion_names)

    if 'category' in request.GET:
        category_names = request.GET['category'].split(',')
        gifts = gifts.filter(category__name__in=category_names)
        current_categories = Category.objects.filter(name__in=category_names)


    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('gifts'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        gifts = gifts.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'gifts': gifts,
        'search_term': query,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'gifts/gift_list.html', context)


def gift_detail(request, gift_id):
    """ A view to show individual gift details """
    gift = get_object_or_404(Gift, pk=gift_id)

    context = {
        'gift': gift,
    }
    return render(request, 'gifts/gift_detail.html', context)

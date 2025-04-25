from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404  # noqa
from django.contrib import messages

from gifts.models import Gift


def view_bag(request):
    """ A view that renders the bag contents"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified gift to the shopping bag """

    gift = get_object_or_404(Gift, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'gift_size' in request.POST:
        size = request.POST['gift_size']

    bag = request.session.get('bag', {})

    if size:
        if item_id in bag:
            if size in bag[item_id]['items_by_size']:
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {gift.name} quantity to   {bag[item_id]["items_by_size"][size]}')  # noqa
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {gift.name} to your bag')  # noqa
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {gift.name} to your bag')  # noqa
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(request, f'Updated {gift.name} quantity to {bag[item_id]}')  # noqa
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {gift.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified gift to the specified amount """

    gift = get_object_or_404(Gift, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'gift_size' in request.POST:
        size = request.POST['gift_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {gift.name} quantity to   {bag[item_id]["items_by_size"][size]}')  # noqa
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {gift.name} from your bag')  # noqa
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {gift.name} quantity to {bag[item_id]}')  # noqa
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {gift.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        gift = get_object_or_404(Gift, pk=item_id)
        size = None
        if 'gift_size' in request.POST:
            size = request.POST['giftsize']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {gift.name} from your bag')  # noqa
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {gift.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item:{e}')
        return HttpResponse(status=500)

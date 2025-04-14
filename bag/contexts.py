from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from gifts.models import Gift

def bag_contents(request):

    bag_items = []
    total = 0
    gift_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():

        if isinstance(item_data, int):
            gift = get_object_or_404(Gift, pk=item_id)
            total += item_data * gift.price
            gift_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'gift': gift,
            })
            
        else:
            gift = get_object_or_404(Gift, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * gift.price
                gift_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'gift': gift,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'gift_count': gift_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
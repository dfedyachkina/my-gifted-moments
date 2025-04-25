from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Gift, Favorite


@login_required
def add_to_favorites(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    Favorite.objects.get_or_create(user=request.user, gift=gift)
    messages.success(request, f'"{gift.name}" has been added to your favorites.')  # noqa
    return redirect('gift_detail', gift_id=gift_id)


def remove_from_favorites(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    Favorite.objects.filter(user=request.user, gift=gift).delete()
    messages.success(request, f'"{gift.name}" has been removed from your favorites.')  # noqa
    next_url = request.GET.get('next') or request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('gift_detail', gift_id=gift_id)


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})  # noqa

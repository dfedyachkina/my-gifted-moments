from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_list, name='favorite_list'),
    path('add/<int:gift_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:gift_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]

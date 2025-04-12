from django.urls import path
from .views import Gifts, GiftDetailView

urlpatterns = [
    path('', Gifts.as_view(), name='gifts'),
    path('gift/<int:pk>/', GiftDetailView.as_view(), name='gift_detail'),
]

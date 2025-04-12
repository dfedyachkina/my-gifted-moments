from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gifts, name='gifts'),
    path('gift/<int:gift_id>/', views.gift_detail, name='gift_detail'),
]

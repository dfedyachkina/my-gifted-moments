from django.contrib import admin
from .models import Occasion, Category, Size, Gift


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'occasion', 'size', 'quantity', 'price', 'image')  # noqa
    list_filter = ('category', 'occasion', 'size')
    search_fields = ('name', 'description')

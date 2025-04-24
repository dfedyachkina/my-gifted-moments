from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    readonly_fields = ['email']

    def has_add_permission(self, request):
        return False
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'date_sent')
    ordering = ('-date_sent',)

    def has_add_permission(self, request):
        return False

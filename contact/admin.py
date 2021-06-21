from django.contrib import admin
from .models import Order


class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'meal', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'meal')
  list_per_page = 25


admin.site.register(Order, ContactAdmin)
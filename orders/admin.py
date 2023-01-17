from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'order_status', 'order_date', 'order_total', 'order_quantity', 'order_address', 'order_city', 'order_state', 'order_zip_code', 'order_phone_number', 'order_email')
    list_display_links = ('order_id', 'user', 'order_status', 'order_date', 'order_total', 'order_quantity', 'order_address', 'order_city', 'order_state', 'order_zip_code', 'order_phone_number', 'order_email')
    list_filter = ('order_id', 'user', 'order_status', 'order_date', 'order_total', 'order_quantity', 'order_address', 'order_city', 'order_state', 'order_zip_code', 'order_phone_number', 'order_email')
    search_fields = ('order_id', 'user', 'order_status', 'order_date', 'order_total', 'order_quantity', 'order_address', 'order_city', 'order_state', 'order_zip_code', 'order_phone_number', 'order_email')
    list_per_page = 25

admin.site.register(Order, OrderAdmin)

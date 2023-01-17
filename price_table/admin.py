from django.contrib import admin
from .models import PriceTable

# Register your models here.
class PriceTableAdmin(admin.ModelAdmin):
    list_display = ('phonemodel', 'storage', 'grade', 'price')
    list_display_links = ('phonemodel', 'storage', 'grade', 'price')
    list_filter = ('phonemodel', 'storage', 'grade')
    search_fields = ('phonemodel', 'storage', 'grade', 'price')
    list_per_page = 25
    

admin.site.register(PriceTable, PriceTableAdmin)
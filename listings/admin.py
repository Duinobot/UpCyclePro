from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'phonemodel', 'storage', 'color', 'grade', 'price_table', 'price', 'sku')
    list_display_links = ('title', 'phonemodel', 'storage', 'color', 'grade', 'price_table', 'sku')
    list_filter = ('phonemodel', 'storage', 'color', 'grade')
    search_fields = ('title', 'phonemodel', 'storage', 'color', 'grade', 'price_table', 'sku')
    list_per_page = 25
    #display the value of price_table.price
    def price(self, obj):
        return obj.price_table.price

    # display the price at detail page
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('price',)

admin.site.register(Listing, ListingAdmin)
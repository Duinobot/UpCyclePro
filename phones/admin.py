from django.contrib import admin
from .models import Phone

# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'phonemodel', 'color', 'storage', 'imei', 'price_table', 'listing', 'grade', 'created_at', 'updated_at')
    list_display_links = ('name', 'slug', 'phonemodel', 'color', 'storage', 'imei', 'price_table', 'listing', 'grade', 'created_at', 'updated_at')
    list_filter =  ('name', 'slug', 'phonemodel', 'color', 'storage', 'imei', 'price_table', 'listing', 'grade', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'phonemodel', 'color', 'storage', 'imei', 'price_table', 'listing', 'grade', 'created_at', 'updated_at')
    list_per_page = 25

    # when phonemodel is seletcted, display the color and storage base on model, using javascript to make it reponsive
    class Media:
        js = ('js/admin.js',)

admin.site.register(Phone, PhoneAdmin)

# Register phone model, color, storage in admin
from django.contrib import admin
from .models import PhoneModel, PhoneColor, PhoneStorage

# Register your models here.
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('model', 'slug')
    list_display_links = ('model', 'slug')
    list_filter = ('model', 'slug')
    search_fields = ('model', 'slug')
    list_per_page = 25

admin.site.register(PhoneModel, PhoneModelAdmin)

class PhoneColorAdmin(admin.ModelAdmin):
    list_display = ('color', 'phonemodel','slug')
    list_display_links = ('color', 'phonemodel','slug')
    list_filter = ('color', 'phonemodel','slug')
    search_fields = ('color', 'phonemodel','slug')
    list_per_page = 25

admin.site.register(PhoneColor, PhoneColorAdmin)

class PhoneStorageAdmin(admin.ModelAdmin):
    list_display = ('storage', 'phonemodel', 'slug')
    list_display_links = ('storage', 'phonemodel', 'slug')
    list_filter = ('storage', 'phonemodel', 'slug')
    search_fields = ('storage', 'phonemodel', 'slug')
    list_per_page = 25

admin.site.register(PhoneStorage, PhoneStorageAdmin)
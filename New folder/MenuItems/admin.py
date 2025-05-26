from django.contrib import admin
from .models import MenuItem
# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'availability')
    search_fields = ('name',)
    list_editable = [ 'price', 'availability']

    list_filter = ('availability',)

admin.site.register(MenuItem, MenuItemAdmin)


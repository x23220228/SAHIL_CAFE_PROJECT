from django.contrib import admin
from .models import MenuItem, Order, Outlet, Reservation

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_filter = ('price',)
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu_item', 'quantity', 'timestamp')

@admin.register(Outlet)
class OutletAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'people', 'datetime', 'outlet']

admin.site.site_header = 'Sahil\'s Cafe Administration'

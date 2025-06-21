from django.contrib import admin
from .models import Owner,Room
# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name', 'email','owner_id')

admin.site.register(Owner, OwnerAdmin)



class RoomAdmin(admin.ModelAdmin):
    list_display = ('pg_name', 'room_type', 'pg_owner', 'total_room', 'is_available')
    list_filter = ('room_type', 'is_available', 'pg_owner')
    search_fields = ('pg_name', 'facility', 'amenity')
    ordering = ('pg_name',)

admin.site.register(Room, RoomAdmin)

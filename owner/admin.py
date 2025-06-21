from django.contrib import admin
from .models import Owner
# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name', 'email','owner_id')

admin.site.register(Owner, OwnerAdmin)

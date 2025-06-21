from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_phone', 'profession','address')
    search_fields = ('user_name', 'user_email', 'profession','address')

admin.site.register(UserDetails, UserDetailsAdmin)

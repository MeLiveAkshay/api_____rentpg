from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api__rentpg.page.page__url')),  # Include your app's URLs
]

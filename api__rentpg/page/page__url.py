from django.urls import path
from . import page__web  # Import views from the same directory
 
urlpatterns = [
    path('', page__web.home),  # No leading slash
]

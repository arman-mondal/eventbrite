from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('api/add_event/', views.add_event, name='add_event'),
]

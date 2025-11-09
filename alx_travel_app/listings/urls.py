from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.PropertyList.as_view(), name='property-list'),
]

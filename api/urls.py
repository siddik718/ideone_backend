from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.create_text, name='create_text'),
    path('text/<str:url>/', views.retrieve_text, name='retrieve_text'),
    path('text/<str:url>/edit/', views.update_text, name='update_text'),
]
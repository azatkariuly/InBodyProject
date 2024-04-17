from django.urls import path
from . import views

urlpatterns = [
    path('', views.handleRequest, name='handle_request'),
]

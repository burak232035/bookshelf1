# bookapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/test/', views.ApiTestView.as_view()),
]
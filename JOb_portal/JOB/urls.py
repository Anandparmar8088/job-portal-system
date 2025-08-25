from django.urls import path, include
from .import views

urlpatterns = [
    path('dt/', views.Job_posting),
]

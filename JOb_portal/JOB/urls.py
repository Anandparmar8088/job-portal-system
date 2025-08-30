from django.urls import path, include
from .import views

urlpatterns = [
    path('job/', views.Job_posting),
    path('get/', views.getjobs),

    
]


# ADMIN : = anand 
# pass  : = 1234

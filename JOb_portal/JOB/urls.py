from django.urls import path, include
from .import views

urlpatterns = [
    path('job/', views.Job_posting),
    path('get/', views.getjobs),
    path('del/<int:id>', views.delete),
    path('delint/<int:id>', views.delete_int),
    path("interested/", views.get_interested),  # list interested jobs
    path("interested/add/<int:job_id>/", views.add_interested),  # add interested job
    path("getcompny/", views.getCompanies),  # show companies
    path("postcompny/", views.postCompanies),  # add companies
    
]









# ADMIN : = anand 
# pass  : = 1234

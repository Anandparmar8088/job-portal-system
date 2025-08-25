
from django.contrib import admin
from django.urls import path, include
# from JOB import urls

urlpatterns = [
    path('api/', include("JOB.urls")),
    path('admin/', admin.site.urls),
]

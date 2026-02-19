
from django.urls import path, include

urlpatterns = [
    path('api/employees/', include('apps.employees.urls')),
    path('api/attendance/', include('apps.attendance.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('ai-intake/', include('ai_intake.urls')),
    path('clinic-staff/', include('clinic_staff.urls')),
]
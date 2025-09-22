from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClinicStaffList.as_view(), name='clinic_staff_list'),
    path('<int:pk>/', views.ClinicStaffDetail.as_view(), name='clinic_staff_detail'),
    path('create/', views.ClinicStaffCreate.as_view(), name='clinic_staff_create'),
    path('update/<int:pk>/', views.ClinicStaffUpdate.as_view(), name='clinic_staff_update'),
    path('delete/<int:pk>/', views.ClinicStaffDelete.as_view(), name='clinic_staff_delete'),
]
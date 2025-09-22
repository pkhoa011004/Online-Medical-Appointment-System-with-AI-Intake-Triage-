from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointments/create/', views.AppointmentCreate.as_view(), name='appointment-create'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdate.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appointment-delete'),
]
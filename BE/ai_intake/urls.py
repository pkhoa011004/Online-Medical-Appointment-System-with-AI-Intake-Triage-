from django.urls import path
from . import views

urlpatterns = [
    path('intake/', views.AIIntakeView.as_view(), name='ai_intake'),
    path('intake/<int:id>/', views.AIIntakeDetailView.as_view(), name='ai_intake_detail'),
]
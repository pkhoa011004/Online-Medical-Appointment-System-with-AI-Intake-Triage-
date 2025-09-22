from django.shortcuts import render
from rest_framework import viewsets
from .models import AIIntake
from .serializers import AIIntakeSerializer

class AIIntakeViewSet(viewsets.ModelViewSet):
    queryset = AIIntake.objects.all()
    serializer_class = AIIntakeSerializer

    def perform_create(self, serializer):
        serializer.save()
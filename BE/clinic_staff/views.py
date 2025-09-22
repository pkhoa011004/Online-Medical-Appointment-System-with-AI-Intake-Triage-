from rest_framework import viewsets
from .models import ClinicStaff
from .serializers import ClinicStaffSerializer

class ClinicStaffViewSet(viewsets.ModelViewSet):
    queryset = ClinicStaff.objects.all()
    serializer_class = ClinicStaffSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
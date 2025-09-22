from rest_framework import serializers
from .models import ClinicStaff

class ClinicStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicStaff
        fields = '__all__'
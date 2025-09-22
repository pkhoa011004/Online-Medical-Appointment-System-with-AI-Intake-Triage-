from rest_framework import serializers
from .models import AIIntake  # Assuming AIIntake is the model for AI intake management

class AIIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIIntake
        fields = '__all__'  # Adjust fields as necessary for your model

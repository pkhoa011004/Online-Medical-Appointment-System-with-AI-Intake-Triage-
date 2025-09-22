from django.db import models

class AIIntake(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    intake_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Intake for {self.patient} on {self.created_at}"
from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_histories', on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    treatment = models.TextField()
    date_diagnosed = models.DateField()

    def __str__(self):
        return f"{self.condition} - {self.patient}"
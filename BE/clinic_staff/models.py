from django.db import models

class ClinicStaff(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Receptionist'),
        ('technician', 'Technician'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_hired = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
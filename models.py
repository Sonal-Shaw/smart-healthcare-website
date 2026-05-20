from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"


class MedicalRecord(models.Model):
    patient_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    prescription = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
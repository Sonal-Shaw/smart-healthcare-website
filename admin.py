from django.contrib import admin
from .models import Doctor, Appointment, MedicalRecord

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'available')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
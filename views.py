from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Doctor, Appointment, MedicalRecord
from django.shortcuts import get_object_or_404

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # simple validation
        if username and password:
            return redirect('doctors')

    return render(request, "djangoapp/login.html")

def signup(request):
    if request.method == "POST":
        # here you could save user data if needed

        return redirect('login')   # redirects to login page

    return render(request, "djangoapp/signup.html")

def index(request):
    return render(request, "djangoapp/index.html")

def doctors(request):
    return render(request, "djangoapp/doctors.html")

def appointments(request):
    return render(request, "djangoapp/appointments.html")

def records(request):
    return render(request, "djangoapp/records.html")

from .models import Appointment

def teleconsult(request):

    appointment = Appointment.objects.order_by('date', 'time').first()
    return render(request, 'djangoapp/teleconsult.html', {
        'appointment': appointment
    })

def book_appointment(request):
    doctors = Doctor.objects.filter(available=True)

    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        doctor = get_object_or_404(Doctor, id=doctor_id)

        Appointment.objects.create(
            patient_name=patient_name,
            doctor=doctor,
            date=date,
            time=time
        )

        return redirect('appointment_list')

    return render(request, 'djangoapp/book_appointment.html', {
        'doctors': doctors
    })

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'djangoapp/appointment_list.html', {
        'appointments': appointments
    })

def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('appointment_list')


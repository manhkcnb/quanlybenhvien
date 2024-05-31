from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient_id', 'doctor_id', 'room_id', 'appointment_date', 'created_at']

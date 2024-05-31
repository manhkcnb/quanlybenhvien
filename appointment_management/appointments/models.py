from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()  # ID của bệnh nhân từ Patient Service
    doctor_id = models.IntegerField()   # ID của bác sĩ từ Doctor Service
    room_id = models.IntegerField()     # ID của phòng từ Room Service
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.id} - Patient {self.patient_id} - Doctor {self.doctor_id} on {self.appointment_date}"

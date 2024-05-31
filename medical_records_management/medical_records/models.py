# medical_records/models.py
from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=100)  # Tên thuốc
    dosage = models.CharField(max_length=100)  # Liều lượng
    frequency = models.CharField(max_length=100)  # Tần suất sử dụng

    def __str__(self):
        return f'{self.name} ({self.dosage} - {self.frequency})'

class MedicalRecord(models.Model):
    patient_id = models.CharField(max_length=100)  # ID bệnh nhân (liên kết tới Quản lý Bệnh nhân)
    doctor_id = models.CharField(max_length=100)  # ID bác sĩ (liên kết tới Quản lý Bác sĩ)
    appointment_id = models.CharField(max_length=100, blank=True, null=True)  # ID lịch hẹn (liên kết tới Quản lý Lịch hẹn)
    visit_date = models.DateField()  # Ngày thăm khám
    diagnosis = models.CharField(max_length=255)  # Chẩn đoán
    treatment = models.TextField()  # Điều trị
    medications = models.ManyToManyField(Medication)  # Danh sách thuốc
    notes = models.TextField()  # Ghi chú

    def __str__(self):
        return f'Record for {self.patient_id} on {self.visit_date}'

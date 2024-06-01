from django.db import models


class MedicalRecord(models.Model):
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    appointment_id = models.CharField(max_length=100, blank=True, null=True)
    visit_date = models.DateField()
    diagnosis = models.CharField(max_length=255)
    treatment = models.TextField()
    medications = models.JSONField()  # Lưu thông tin thuốc dưới dạng JSON
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "Medical Records"

    def __str__(self):
        return f'Record for {self.patient_id} on {self.visit_date}'

    @property
    def medications_info(self):
        if self.medications:
            return [f"Medication ID: {medication['medication_id']}, Dosage: {medication['dosage']}, Frequency: {medication['frequency']}" for medication in self.medications]
        else:
            return []
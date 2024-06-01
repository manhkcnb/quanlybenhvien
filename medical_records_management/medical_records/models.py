from django.db import models

class Treatment(models.Model):
    treatmentName = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    usage = models.TextField()
    medical_record = models.ForeignKey('MedicalRecord', related_name='treatments', on_delete=models.CASCADE)

    def __str__(self):
        return self.treatmentName

class MedicalRecord(models.Model):
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    appointment_id = models.CharField(max_length=100, blank=True, null=True)
    visit_date = models.DateField()
    diagnosis = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "Medical Records"

    def __str__(self):
        return f'Record for {self.patient_id} on {self.visit_date}'

    @property
    def medications_info(self):
        return [f"Medication: {med.name}, Dosage: {med.dosage}, Frequency: {med.frequency}" for med in self.medications.all()]

class MedicalHistory(models.Model):
    medical_record = models.OneToOneField(MedicalRecord, on_delete=models.CASCADE)
    familyMH = models.TextField()
    personalMH = models.TextField()
    allergies = models.TextField()
    immunizations = models.TextField()

    def __str__(self):
        return f"Medical history for {self.medical_record}"

class Medication(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, related_name='medications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name

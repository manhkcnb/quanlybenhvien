from rest_framework import serializers
from .models import MedicalRecord
import requests

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_info = serializers.SerializerMethodField()
    doctor_info = serializers.SerializerMethodField()
    medications_info = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient_id', 'patient_info', 'doctor_id', 'doctor_info', 'visit_date', 'diagnosis', 'treatment', 'medications', 'notes','medications_info']
        read_only_fields = ['id', 'medications_info']
    def get_patient_info(self, obj):
        patient_id = obj.patient_id
        patient_info = self._get_api_data(f'http://127.0.0.1:8006/api/patients/{patient_id}')
        return patient_info

    def get_doctor_info(self, obj):
        doctor_id = obj.doctor_id
        doctor_info = self._get_api_data(f'http://127.0.0.1:8003/api/doctors/{doctor_id}')
        return doctor_info

    def get_medications_info(self, obj):
        medications_info = []
        if obj.medications:
            for medication in obj.medications:
                medication_id = medication.get('medication_id')
                dosage = medication.get('dosage')
                frequency = medication.get('frequency')
                medication_info = self._get_medication_info(medication_id)
                medication_info['dosage'] = dosage
                medication_info['frequency'] = frequency
                medications_info.append(medication_info)
        return medications_info

    
    def _get_medication_info(self, medication_id):
        try:
            response = requests.get(f'http://127.0.0.1:8005/api/medicine/{medication_id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching medication info for medication_id {medication_id}: {e}")
            return {}
    def _get_api_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-200 responses
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., network issues, server errors)
            print(f"Error fetching data from {url}: {e}")
            return {}  # Return empty dictionary if there's an error
        except ValueError as e:
            # Handle JSON decoding errors
            print(f"Error decoding JSON from {url}: {e}")
            return {}  # Return empty dictionary if there's an error

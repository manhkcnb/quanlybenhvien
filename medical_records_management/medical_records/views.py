# medical_records/views.py
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

PATIENT_SERVICE_URL = 'http://127.0.0.1:8006/api/patients/'
DOCTOR_SERVICE_URL = 'http://127.0.0.1:8003/api/doctors/'
MEDICINE_SERVICE_URL = 'http://127.0.0.1:8005/api/medicine/'

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_patient_info(self, patient_id):
        return self.get_api_data(PATIENT_SERVICE_URL, patient_id)

    def get_doctor_info(self, doctor_id):
        return self.get_api_data(DOCTOR_SERVICE_URL, doctor_id)

    def get_medicine_name(self, medicine_id):
        return self.get_api_data(MEDICINE_SERVICE_URL, medicine_id)

    def get_api_data(self, url, resource_id):
        response = requests.get(f'{url}{resource_id}')
        if response.status_code == 200:
            return response.json()
        return {}

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def patients_list(self, request):
        return self.get_api_data(PATIENT_SERVICE_URL, '')

    @action(detail=False, methods=['get'])
    def doctors_list(self, request):
        return self.get_api_data(DOCTOR_SERVICE_URL, '')

    @action(detail=False, methods=['get'])
    def medicines_list(self, request):
        return self.get_api_data(MEDICINE_SERVICE_URL, '')

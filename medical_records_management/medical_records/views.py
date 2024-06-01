# Import các thư viện và modules cần thiết
import requests  # Sử dụng để gửi yêu cầu HTTP đến các dịch vụ khác
from rest_framework import viewsets, status  # Cung cấp lớp base cho viewset
from rest_framework.response import Response  # Để trả về phản hồi HTTP
from rest_framework.decorators import action  # Để định nghĩa các hành động tùy chỉnh
from .models import MedicalRecord, Treatment, Medication, MedicalHistory  # Import models
from .serializers import MedicalRecordSerializer, TreatmentSerializer, MedicationSerializer, MedicalHistorySerializer  # Import serializers

# Định nghĩa các URL cho các dịch vụ khác nhau
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
        return {}  # Trả về một từ điển rỗng nếu không thể lấy dữ liệu từ dịch vụ

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
        data = self.get_api_data(PATIENT_SERVICE_URL, '')
        return Response(data)

    @action(detail=False, methods=['get'])
    def doctors_list(self, request):
        data = self.get_api_data(DOCTOR_SERVICE_URL, '')
        return Response(data)

    @action(detail=False, methods=['get'])
    def medicines_list(self, request):
        data = self.get_api_data(MEDICINE_SERVICE_URL, '')
        return Response(data)

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

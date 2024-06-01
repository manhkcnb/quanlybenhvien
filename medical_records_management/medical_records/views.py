# medical_records/views.py

# Import các thư viện và modules cần thiết
import requests  # Sử dụng để gửi yêu cầu HTTP đến các dịch vụ khác
from rest_framework import viewsets, status  # Cung cấp lớp base cho viewset
from rest_framework.response import Response  # Để trả về phản hồi HTTP
from rest_framework.decorators import action  # Để định nghĩa các hành động tùy chỉnh
from .models import MedicalRecord  # Import model MedicalRecord
from .serializers import MedicalRecordSerializer  # Import serializer cho MedicalRecord

# Định nghĩa các URL cho các dịch vụ khác nhau
PATIENT_SERVICE_URL = 'http://127.0.0.1:8006/api/patients/'
DOCTOR_SERVICE_URL = 'http://127.0.0.1:8003/api/doctors/'
MEDICINE_SERVICE_URL = 'http://127.0.0.1:8005/api/medicine/'

# Định nghĩa lớp MedicalRecordViewSet, kế thừa từ viewsets.ModelViewSet của Django REST framework
class MedicalRecordViewSet(viewsets.ModelViewSet):
    # Queryset cho viewset, lấy tất cả các bản ghi MedicalRecord từ cơ sở dữ liệu
    queryset = MedicalRecord.objects.all()
    # Serializer cho viewset, sử dụng MedicalRecordSerializer để serialize/deserialize dữ liệu
    serializer_class = MedicalRecordSerializer

    # Phương thức để lấy thông tin của một bệnh nhân dựa trên ID
    def get_patient_info(self, patient_id):
        return self.get_api_data(PATIENT_SERVICE_URL, patient_id)

    # Phương thức để lấy thông tin của một bác sĩ dựa trên ID
    def get_doctor_info(self, doctor_id):
        return self.get_api_data(DOCTOR_SERVICE_URL, doctor_id)

    # Phương thức để lấy tên của một loại thuốc dựa trên ID
    def get_medicine_name(self, medicine_id):
        return self.get_api_data(MEDICINE_SERVICE_URL, medicine_id)

    # Phương thức để gửi yêu cầu HTTP và lấy dữ liệu từ một dịch vụ khác
    def get_api_data(self, url, resource_id):
        response = requests.get(f'{url}{resource_id}')
        if response.status_code == 200:
            return response.json()
        return {}  # Trả về một từ điển rỗng nếu không thể lấy dữ liệu từ dịch vụ

    # Phương thức để lấy danh sách tất cả các bản ghi MedicalRecord
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Phương thức để tạo một bản ghi MedicalRecord mới
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Định nghĩa một action tùy chỉnh để lấy danh sách bệnh nhân
    @action(detail=False, methods=['get'])
    def patients_list(self, request):
        data = self.get_api_data(PATIENT_SERVICE_URL, '')
        return Response(data)

    # Định nghĩa một action tùy chỉnh để lấy danh sách bác sĩ
    @action(detail=False, methods=['get'])
    def doctors_list(self, request):
        data = self.get_api_data(DOCTOR_SERVICE_URL, '')
        return Response(data)

    # Định nghĩa một action tùy chỉnh để lấy danh sách các loại thuốc
    @action(detail=False, methods=['get'])
    def medicines_list(self, request):
        data = self.get_api_data(MEDICINE_SERVICE_URL, '')
        return Response(data)

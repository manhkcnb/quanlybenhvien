from rest_framework import viewsets
from .models import Doctor, Department
from .serializers import DoctorSerializer ,DepartmentSerializer, DepartmentCreateSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return DepartmentCreateSerializer
        return DepartmentSerializer
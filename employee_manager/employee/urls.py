# urls.py
from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/employees/', EmployeeListCreateAPIView.as_view(), name='employee_list'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee_detail'),
]

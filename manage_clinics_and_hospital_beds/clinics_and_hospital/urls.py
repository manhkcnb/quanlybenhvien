# urls.py
from django.urls import path
from .views import ClinicListCreateAPIView, ClinicRetrieveUpdateDestroyAPIView, \
                   BedListCreateAPIView, BedRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/clinics/', ClinicListCreateAPIView.as_view(), name='clinic_list'),
    path('api/clinics/<int:pk>/', ClinicRetrieveUpdateDestroyAPIView.as_view(), name='clinic_detail'),
    path('api/beds/', BedListCreateAPIView.as_view(), name='bed_list'),
    path('api/beds/<int:pk>/', BedRetrieveUpdateDestroyAPIView.as_view(), name='bed_detail'),
]

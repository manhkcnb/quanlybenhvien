from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet, TreatmentViewSet, MedicationViewSet, MedicalHistoryViewSet

router = DefaultRouter()
router.register(r'records', MedicalRecordViewSet)
router.register(r'treatments', TreatmentViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'medicalhistories', MedicalHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

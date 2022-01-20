from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from rest_framework.viewsets import ModelViewSet

from patient_records.models import (
    Patient, 
    ProblemList,
    VitalSign,
    SocialHistory,
    MedicationStatement,
    MedicationItem
)
from .apiserializers import (
    PatientSerializer,  
    ProblemListSerializer,
    VitalSignSerializer,
    SocialHistorySerializer,
    MedicationStatementSerializer,
    MedicationItemSerializer
)

# Create your views here.


class    PatientViewSet(ModelViewSet):
    serializer_class =    PatientSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(   Patient, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return    Patient.objects.filter()

class     ProblemListViewSet(ModelViewSet):
    serializer_class =     ProblemListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    ProblemList, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     ProblemList.objects.filter()

class     MedicationItemViewSet(ModelViewSet):
    serializer_class =     MedicationItemSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    MedicationItem, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     MedicationItem.objects.filter()

class     VitalSignViewSet(ModelViewSet):
    serializer_class =     VitalSignSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    VitalSign, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     VitalSign.objects.filter()
class     SocialHistoryViewSet(ModelViewSet):
    serializer_class =     SocialHistorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    SocialHistory, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     SocialHistory.objects.filter()
class     MedicationStatementViewSet(ModelViewSet):
    serializer_class =     MedicationStatementSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    MedicationStatement, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     MedicationStatement.objects.filter()

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from rest_framework.viewsets import ModelViewSet

from .models import (
    InternationalPatientSummary, 
    EPrescription, 
    ProblemList,
    VitalSigns,
    SocialHistory,
    MedicationStatement
)
from .serializers import (
    InternationalPatientSummarySerializer, 
    EPrescriptionSerializer, 
    ProblemListSerializer,
    VitalSignsSerializer,
    SocialHistorySerializer,
    MedicationStatementSerializer
)

# Create your views here.


class     EPrescriptionViewSet(ModelViewSet):
    serializer_class =     EPrescriptionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    EPrescription, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     EPrescription.objects.filter()

class     ProblemListViewSet(ModelViewSet):
    serializer_class =     ProblemListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    ProblemList, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     ProblemList.objects.filter()

class     InternationalPatientSummaryViewSet(ModelViewSet):
    serializer_class =     InternationalPatientSummarySerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    InternationalPatientSummary, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     InternationalPatientSummary.objects.filter()

class     VitalSignsViewSet(ModelViewSet):
    serializer_class =     VitalSignsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(    VitalSigns, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return     VitalSigns.objects.filter()
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

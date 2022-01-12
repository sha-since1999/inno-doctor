from rest_framework import serializers
from .models import (
    InternationalPatientSummary, 
    EPrescription, 
    ProblemList,
    VitalSigns,
    SocialHistory,
    MedicationStatement
)
class InternationalPatientSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalPatientSummary
        fields = '__all__'
        
class EPrescriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EPrescription
        fields = '__all__'
        
class ProblemListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProblemList
        fields = '__all__'

class SocialHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialHistory
        fields = '__all__'


class MedicationStatementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicationStatement
        fields = '__all__'


class VitalSignsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VitalSigns
        fields = '__all__'


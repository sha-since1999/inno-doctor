from rest_framework import serializers
from patient_records.models import (
    MedicationItem,
    Patient, 
    ProblemList,
    VitalSign,
    SocialHistory,
    MedicationStatement
)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
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


class MedicationItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicationItem
        fields = '__all__'


class VitalSignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VitalSign
        fields = '__all__'


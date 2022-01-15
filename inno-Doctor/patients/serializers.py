from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ( 'name', 'aadhaarId', 'dob' , 'gender','last_udpated_on')
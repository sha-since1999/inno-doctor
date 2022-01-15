from django.forms import ModelForm

from .models import (MedicationItem, Patient,
                     ProblemList,
                     VitalSign, SocialHistory, MedicationStatement, )


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
class MedicationItemForm(ModelForm):
    class Meta:
        model = MedicationItem
        fields = '__all__'

class MedicationStatementForm(ModelForm):
    class Meta:
        model = MedicationStatement
        fields = ("patient",)
        
class ProblemListForm(ModelForm):
    class Meta:
        model = ProblemList
        fields = '__all__'
        


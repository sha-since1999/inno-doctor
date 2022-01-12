from django.forms import ModelForm, forms
from .models import (
    InternationalPatientSummary, 
    EPrescription, 
    ProblemList,
    VitalSigns,
    SocialHistory,
    MedicationStatement
)

class InternationalPatientSummaryForm(ModelForm):
    class Meta:
        model = InternationalPatientSummary
        fields = '__all__'
        
class EPrescriptionForm(forms.ModelForm):
    
    class Meta:
        model = EPrescription
        fields = '__all__'
        
class ProblemListForm(forms.ModelForm):
    
    class Meta:
        model = ProblemList
        fields = '__all__'

class SocialHistoryForm(forms.ModelForm):
    
    class Meta:
        model = SocialHistory
        fields = '__all__'


class MedicationStatementForm(forms.ModelForm):
    
    class Meta:
        model = MedicationStatement
        fields = '__all__'


class VitalSignsForm(forms.ModelForm):
    
    class Meta:
        model = VitalSigns
        fields = '__all__'

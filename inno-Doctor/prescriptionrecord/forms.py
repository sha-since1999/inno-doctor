from django import forms
from ..patient_records.models import *

class MedItem(forms.ModelForm):
    class Meta:
        model = MedicationItem
        fields = ('medication_item', 'name', 'form','category','unit_of_prescription','batch_id','expiry','dose_amount', 'dose_duration','dose_unit','dose_frequency','dose_interval','dose_specific_timing','route','body_site' )
        
        widgets ={
            'medication_item': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'form': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'unit_of_prescription': forms.TextInput(attrs={'class':'form-control'}),
            'batch_id': forms.TextInput(attrs={'class':'form-control'}),
            'expiry': forms.TextInput(attrs={'class':'form-control'}),
            'dose_amount': forms.TextInput(attrs={'class':'form-control'}),
            'dose_duration': forms.TextInput(attrs={'class':'form-control'}),
            'dose_unit': forms.TextInput(attrs={'class':'form-control'}),
            'dose_frequency': forms.TextInput(attrs={'class':'form-control'}),
            'dose_interval': forms.TextInput(attrs={'class':'form-control'}),
            'dose_specific_timing': forms.TextInput(attrs={'class':'form-control'}),
            'route': forms.TextInput(attrs={'class':'form-control'}),
            'body_site': forms.TextInput(attrs={'class':'form-control'}),

        }
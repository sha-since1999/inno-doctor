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
        
    # def __init__(self, *args, **kwargs):
    #     """Populating the choices of  the favorite_choices field using the favorites_choices kwargs"""
    #     favorites_choices = kwargs.pop('medication_item')
    #     super().__init__(*args, **kwargs)
    #     self.fields['medication_item'].choices = favorites_choices

class MedicationStatementForm(ModelForm):
    class Meta:
        model = MedicationStatement
        fields = ("patient",)
        
class ProblemListForm(ModelForm):
    class Meta:
        model = ProblemList
        fields = '__all__'
        
class SocialHistoryForm(ModelForm):
    
    class Meta:
        model = SocialHistory
        fields = '__all__'
        
class VitalSignForm(ModelForm):
    
    class Meta:
        model = VitalSign
        fields = {'body_weight',
                'height',
                'respiration_rate',
                'pulse_rate',
                'body_temperature',
                'head_circumference',
                'pulse_oximetry',
                'body_mass_index',
                'blood_pressure_systolic',
                'blood_pressure_diastolic' 
                }



from django.forms import ModelForm, DateField
import datetime
from .models import (MedicationItem, Patient,
                     ProblemList,
                     VitalSign, SocialHistory, MedicationStatement, )
from django.forms.models import inlineformset_factory

class PatientForm(ModelForm):
    # date_of_birth = DateField(initial=datetime.date.today) 
    class Meta:
        model = Patient
        fields = ['aadhaarId', 'name', 'gender', 'date_of_birth']
        # widgets = {'date_of_birth': DateField(datetime.date.today)}
        
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
        fields = ['problem', 'body_site', 'severity', 'abatement_date', 'diagnostic_certainty',]
        
class SocialHistoryForm(ModelForm):
    
    class Meta:
        model = SocialHistory
        fields = ['tobacco_smoking_status', 'alcohol_consumption_status', 'alcohol_consumption_unit', 'alcohol_consumption_frequency']

class VitalSignForm(ModelForm):
    
    class Meta:
        model = VitalSign
        fields = ['body_weight', 'height', 'respiration_rate', 'pulse_rate', 'body_temperature', 'head_circumference', 'pulse_oximetry', 'body_mass_index', 'blood_pressure_systolic', 'blood_pressure_diastolic',]



MedicationStatementFormSet = inlineformset_factory(MedicationStatement, 
                                                       MedicationItem, 
                                                       fields=(
                                                           'medication_item', 
                                                           'name', 
                                                           'form', 
                                                           'category', 
                                                           'unit_of_prescription', 
                                                           'batch_id', 
                                                           'expiry',
                                                           'dose_amount',
                                                           'dose_duration',
                                                           'dose_unit', 
                                                           'dose_frequency',
                                                           'dose_interval',
                                                           'dose_specific_timing',
                                                           'route',
                                                           'body_site'
                                                       ),
                                                        extra=5
                                                   )
from django.forms import ModelForm
from .models import VitalSigns
from django import forms

class VitalSignsForm(ModelForm):
    class Meta:
        model = VitalSigns
        fields = '__all__'
        # fields = ('body_weight','ips', 'height', 'respiration_rate','pulse_rate','body_temperature','head_circumference','pulse_oximetry','body_mass_index', 'blood_pressure_systolic','blood_pressure_diastolic')
        
        # widgets ={
        #     'body_weight': forms.TextInput(attrs={'class':'form-control'}),
        #     'ips': forms.TextInput(attrs={'class':'form-control'}),
        #     # 'ips': forms.HiddenInput(),
        #     'height': forms.TextInput(attrs={'class':'form-control'}),
        #     'respiration_rate': forms.TextInput(attrs={'class':'form-control'}),
        #     'pulse_rate': forms.TextInput(attrs={'class':'form-control'}),
        #     'body_temperature': forms.TextInput(attrs={'class':'form-control'}),
        #     'head_circumference': forms.TextInput(attrs={'class':'form-control'}),
        #     'pulse_oximetry': forms.TextInput(attrs={'class':'form-control'}),
        #     'body_mass_index': forms.TextInput(attrs={'class':'form-control'}),
        #     'blood_pressure_systolic': forms.TextInput(attrs={'class':'form-control'}),
        #     'blood_pressure_diastolic': forms.TextInput(attrs={'class':'form-control'}),
        # }
    # def __init__(self, *args, **kwargs):
    #     from django.forms.widgets import HiddenInput
    #     hide_condition = kwargs.pop('hide_condition',None)
    #     super(VitalSignsForm, self).__init__(*args, **kwargs)
    #     if hide_condition:
    #         self.fields['ips'].widget = HiddenInput()
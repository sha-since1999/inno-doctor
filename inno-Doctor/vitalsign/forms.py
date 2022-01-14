from django.forms import ModelForm
from ..patient_records.models import VitalSigns

class VitalSignsForm(ModelForm):
    class Meta:
        model = VitalSigns
        fields = '__all__'
from django.forms import ModelForm
from .models import SocialHistory, VitalSigns

class VitalSignsForm(ModelForm):
    class Meta:
        model = VitalSigns
        fields = '__all__'

class SocialHistoryForm(ModelForm):
    class Meta:
        model = SocialHistory
        fields = '__all__'

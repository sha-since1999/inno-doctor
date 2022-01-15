from django.forms import ModelForm
from .models import ProblemList, SocialHistory, VitalSigns

class VitalSignsForm(ModelForm):
    class Meta:
        model = VitalSigns
        fields = '__all__'

class SocialHistoryForm(ModelForm):
    class Meta:
        model = SocialHistory
        fields = '__all__'


class ProblemListForm(ModelForm):
    class Meta:
        model = ProblemList
        fields = '__all__'

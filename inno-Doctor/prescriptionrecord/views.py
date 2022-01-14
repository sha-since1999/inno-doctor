from django.shortcuts import render

# Create your views here.
from ..patient_records.models import *
from .forms import MedItem

# class MedStateView(CreateView):
#     model = MedicationStatement
#     form_class = MedState
#     template_name = 'accounts/medstate.html'

def med_form(request):
    if request.method=='POST':
        form = MedItem(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=MedItem
    return render(request, 'prescription_form.html', {'form': form})
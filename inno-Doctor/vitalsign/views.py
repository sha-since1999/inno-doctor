from django.shortcuts import render, redirect
from ..patient_records.models import VitalSigns
from .forms import VitalSignsForm
from django.contrib import messages
# Create your views here.

def VitalSignPage(request):  
    if request.method == "POST":  
        form = VitalSignsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                messages.success(request, 'Vital signs are successfully added.!')
                model = form.instance
                return redirect('/')  
            except:  
                messages.error(request, 'failed to add vital signs')
    else:  
        form = VitalSignsForm()  
    return render(request,'vital-sign.html',{'form':form})
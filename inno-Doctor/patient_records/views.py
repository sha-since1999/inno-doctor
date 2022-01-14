from django.shortcuts import render,  redirect
from .models import  (MedicationItem,
                      MedicationStatement, VitalSigns )
from django.contrib import messages
from .forms import SocialHistoryForm, VitalSignsForm
from patients.models import Patient
# Create your views here.
def PatientView(request):
    return render(request, "patient_records/patient_record_form.html")

def PatientList(request):
    aadhar_no = request.POST.get('aadharid')
    date_of_birth=request.POST.get('bdate')
    if (Patient.objects.filter(aadhaarId=aadhar_no).exists()) and (
            Patient.objects.filter(dob=date_of_birth).exists()):
        ips = Patient.objects.get(
                aadhaarId = aadhar_no
        )
        medication_id = MedicationStatement.objects.filter(
                ips=ips
        ).values_list('id', flat = True).order_by(
                '-timestamp')[:1]
        medication_items = MedicationItem.objects.filter(
                medication_statement_id=medication_id)
        args = {'medication_items': medication_items }
        return render(request, "patient_records/patient_record_list.html", args)
    else:
        messages.error(request, 'Patient is not registered')
        return render(request, "patient_records/patient_record_form.html")


def VitalSignPage(request):
    if request.method == "POST":  
        form = VitalSignsForm(request.POST)
        if form.is_valid():  
            try:
                form.save()
                messages.success(request, 'Vital signs are successfully added.!')
                return redirect('/')  
            except:  
                messages.error(request, 'failed to add vital signs')
    else:  
        form = VitalSignsForm()  
    return render(request,"patient_records/vital_signf.html",{'form':form})


def SocialHistoryPage(request):
    if request.method == "POST":
        form = SocialHistoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, 'Social History added successfully!'
                    )
                return redirect('/')
            except:
                messages.error(request, 'failed to add social history')
    else:
        form = SocialHistoryForm()
    return render(request, "patient_records/social_history.html", {'form':form})

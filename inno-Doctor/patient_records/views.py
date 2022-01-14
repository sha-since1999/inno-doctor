from django.shortcuts import render,  redirect
from .models import  (MedicationItem,
                      MedicationStatement, VitalSigns )
from django.contrib import messages
from .forms import VitalSignsForm
from patients.models import Patient
# Create your views here.
def PatientView(request):
    return render(request, "patient_records/patient_record_form.html")

def PatientList(request):
    aadhar_no = request.POST.get('aadharid')
    date_of_birth=request.POST.get('bdate')
    if (Patient.objects.filter(aadhar_no=aadhar_no).exists()) and (Patient.objects.filter(date_of_birth=date_of_birth).exists()):
        ips_id = Patient.objects.get(
                aadhar_no = aadhar_no
        ).id
        medication_id = MedicationStatement.objects.filter(
                ips_id = ips_id
        ).values_list('id', flat = True).order_by(
                '-timestamp')[:1]
        medication_items = MedicationItem.objects.filter(
                medication_statement_id=medication_id)
        my_values = [item.dose_amount for item in medication_items]
        args = {'medication_items': medication_items }
        return render(request, "patient_records/patient_record_list.html", args)
    else:
        messages.error(request, 'Patient is not registered')
        return render(request, "patient_records/patient_record_form.html")


def VitalSignPage(request, id):
    patient = Patient.objects.get(aadhaarId=id)

#     form = VitalSignsForm(initial={'height': patient.name, })
    print("lll", patient.aadhaarId)
    if request.method == "POST":  
        form = VitalSignsForm(request.POST)  
        # print("zzz", form.height)
        print(form['height'].value())
        # form.data['ips'] = patient
        print(form.data['ips'])
        print("iiioo", form)
        if form.is_valid():  
            try:  
                # instance = form.save(commit="false")
                # print("jhdj", instance)
                # instance.ips=patient
                # instance.save()   

                form.save() 
                messages.success(request, 'Vital signs are successfully added.!')
                model = form.instance
                return redirect('/')  
            except:  
                messages.error(request, 'failed to add vital signs')
    else:  
        form = VitalSignsForm()  
    return render(request,"patient_records/vital_signf.html",{'form':form})
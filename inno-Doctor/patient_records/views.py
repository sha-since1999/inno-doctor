from django.shortcuts import render

# Create your views here.
def PatientView(request):
    return render(request, "patient_records/patient_record_form.html")

def PatientList(request):
    aadhar_no = request.POST.get('aadharid')
    date_of_birth=request.POST.get('bdate')
    if (InternationalPatientSummary.objects.filter(aadhar_no=aadhar_no).exists()) and (InternationalPatientSummary.objects.filter(date_of_birth=date_of_birth).exists()):
        ips_id = InternationalPatientSummary.objects.get(
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

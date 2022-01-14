from django.shortcuts import render
from .models import  (MedicationItem,
                     InternationalPatientSummary, MedicationStatement, )
from django.contrib import messages


# Create your views here.
def PatientView(request):
    return render(request, "patient_records/patient_record_form.html")

def PatientList(request):
    aadhar_no = request.POST.get('aadharid')
    date_of_birth=request.POST.get('bdate')
    print(date_of_birth)
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

def EPrescription(request, aadhar_no):
    ips = InternationalPatientSummary.objects.filter(aadhar_no=aadhar_no)
    if ips:
        medication_statement = MedicationStatement.objects.create(ips=ips[0])
        medication_items = []
        for item in request.POST.get('items'):
            med_item = MedicationItem(name=item["name"], form=item["form"],
                                      medication_statement=medication_statement,
                                      category=item["category"],
                                      unit_of_prescription=item["unit_of_prescription"],
                                      batch_id=item["batch_id"],
                                      expiry=item["expiry"],
                                      dose_amount=item["dose_amount"],
                                      dose_duration=item["dose_duration"],
                                      dose_unit=item["dose_unit"],
                                      dose_frequency=item.get("dose_frequency"),
                                      dose_interval=item.get("dose_interval"),
                                      dose_specific_timing=item.get(
                                              "dose_specific_timing"),
                                      route=item["route"],
                                      body_site=item["body_site"])

            medication_items.append(med_item)
        MedicationItem.objects.bulk_create(medication_items)
    else:
        raise ValueError

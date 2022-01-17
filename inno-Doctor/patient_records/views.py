from email.message import Message
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.urls import reverse

from django.shortcuts import  redirect
from .models import Patient

from django.shortcuts import render

from .forms import (MedicationItemForm, PatientForm,
                    SocialHistoryForm,VitalSignForm,
                     ProblemListForm,
                      MedicationStatementForm, )

from .models import (MedicationItem, Patient,
                     ProblemList,
                     VitalSign, SocialHistory, MedicationStatement, )


from django.contrib import messages


# Create your views here.
def eprescriptionList(request, id):  
    patient = Patient.objects.get(aadhaarId=id)
    try:
        # medicationStatements=get_object_or_404(MedicationStatement, patient=patient)
        medicationstatements=MedicationStatement.objects.filter(patient= patient)
        medicationitems=[]
        medication_statement_ids=[]
        for medicationstatement in medicationstatements:
            medicationitem = MedicationItem.objects.filter(medication_statement=medicationstatement)
            medication_statement_ids.append(medicationstatement.id)
            if medicationitem is not None:
                medicationitems.append(medicationitem)
        print(medicationitems)
        return render(request,"patient_records/eprescription.html" ,context={"medicationStatementIds":medication_statement_ids, "medicationItems": medicationitems,'aadhaarId':id})
    except:
            messages.error(request, 'no medication statemtment found!') 
    return  redirect('/patient_records/patient-detail/{}'.format(id))  

def patientDetails(request):

    if request.method == "POST":  
        id= request.POST['aadhaarId']
        try:
            patient= get_object_or_404(Patient,aadhaarId=id)
            return render(request,"patient_records/patient-details.html",context={'patient':patient})  
        except:
            messages.error(request, 'patient record found')
    return redirect('/patient_records/patient-check')  
         
         
def patientDetail(request , id)  : 
    try:
        patient= get_object_or_404(Patient,aadhaarId=id)
        return render(request,"patient_records/patient-details.html",context={'patient':patient})  
    except:
        messages.error(request, 'patient record found')
        
    return redirect('/patient_records/patient-check')  

        
def patientCheck(request):  
    patients = Patient.objects.all()  
    return render(request , "patient_records/patient-check.html",{'patients':patients})  

def patientCreate(request):  
    if request.method == "POST":  
        form = PatientForm(request.POST)  
        id= request.POST['aadhaarId']
        if form.is_valid():  
            try:  
                form.save() 
                messages.success(request, 'New Patient is successfully added.!')
                model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id))  
            except:  
                messages.error(request, 'failed to add patient')
    else:  
        form = PatientForm()  
    return render(request,'patient_records/patient-create.html',{'form':form})  

def patientUpdate(request, id):  
    patient = Patient.objects.get(aadhaarId=id)
    form = PatientForm(initial={'name': patient.name, 'aadhaarId': patient.aadhaarId, 'date_of_birth': patient.date_of_birth, 'gender': patient.gender})
    if request.method == "POST":  
        form = PatientForm(request.POST, instance=patient)  
        if form.is_valid():  
            try:  
                form.save() 
                # model = form.instance
                messages.success(request,'patient updated!')
                return redirect('/patient_records/patient-check')  
            except Exception as e: 
                messages.error(request,'update error!')
    return render(request,'patient_records/patient-update.html',{'form':form})  


def PatientView(request):
    return render(request, "patient_records/patient_record_form.html")

def PatientList(request):
    aadhaarId = request.POST.get('aadharid')
    date_of_birth=request.POST.get('bdate')
    if (Patient.objects.filter(aadhaarId=aadhaarId).exists()) and (Patient.objects.filter(date_of_birth=date_of_birth).exists()):
        # ips_id = Patient.objects.get(
        #         aadhaarId = aadhaarId
        # ).id
        medication_id = MedicationStatement.objects.filter(
                patient_id = aadhaarId
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



def patientProblemListCreate(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    
    if request.method == "POST":  
        form = ProblemListForm(request.POST, initial={ 'patient':patient })  
        if form.is_valid():  
            try:  
                obj=form.save( commit=False) 
                obj.patient =Patient.objects.get(aadhaarId=id)
                obj.save()
                messages.success(request, 'New ProblemList is successfully added.!')
                # model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id))   
            except:  
                messages.error(request, 'failed to add problem list')
    else:  
        form = ProblemListForm( initial={ 'patient':patient } )  
    return render(request,'patient_records/patient-problem-list.html',{'form':form,'patient' :patient})  

def patientSocialHistoryCreate(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    
    if request.method == "POST":  
        form = SocialHistoryForm(request.POST, initial={ 'patient':patient })  
        if form.is_valid():  
            try:  
                obj=form.save( commit=False) 
                obj.patient =Patient.objects.get(aadhaarId=id)
                obj.save()
                messages.success(request, 'New Social History is successfully added.!')
                # model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id)) 
            except:  
                messages.error(request, 'failed to add Social History list')
    else:  
        form = SocialHistoryForm( initial={ 'patient':patient } )  
    return render(request,'patient_records/patient-social-history-list.html',{'form':form,'patient' :patient})  

def patientVitalSignCreate(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    
    if request.method == "POST":  
        form = VitalSignForm(request.POST, initial={ 'patient':patient })  
        if form.is_valid():  
            try:  
                obj=form.save( commit=False) 
                obj.patient =Patient.objects.get(aadhaarId=id)
                obj.save()
                messages.success(request, 'New Vital Sign is successfully added.!')
                # model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id)) 
            except:  
                messages.error(request, 'failed to add vital sign')
    else:  
        form = VitalSignForm( initial={ 'patient':patient } )  
    return render(request,'patient_records/patient-vital-sign.html',{'form':form,'patient' :patient})  


def patientSocialHistoryUpdate(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    socialhistory= SocialHistory.objects.get(patient=patient)
    form= SocialHistoryForm( initial = {'patient':patient, 'tobacco_smoking_status':socialhistory.tobacco_smoking_status,'alcohol_consumption_status':socialhistory,'alcohol_consumption_unit':socialhistory.alcohol_consumption_unit, 'alcohol_consumption_frequency':socialhistory.alcohol_consumption_frequency} )
    if request.method == "POST":  
        form = SocialHistoryForm(request.POST, instance=socialhistory)  
        if form.is_valid():  
            try:  
                form.save()
                messages.success(request, 'New Social History is successfully Updated.!')
                # model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id)) 
            except:  
                messages.error(request, 'failed to Update Social History list')
    return render(request,'patient_records/genralForm.html',{'form':form,'patient' :patient})  

def patientVitalSignUpdate(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    vitalsign= VitalSign.objects.get(patient= patient)
    form= VitalSignForm(initial={'patient':patient ,'body_weight':vitalsign.body_weight,'height':vitalsign.height,'respiration_rate':vitalsign.respiration_rate,'pulse_rate':vitalsign.pulse_rate,'body_temperature':vitalsign.body_temperature,'head_circumference':vitalsign.head_circumference,'pulse_oximetry':vitalsign.pulse_oximetry,'body_mass_index':vitalsign.body_mass_index,'blood_pressure_systolic':vitalsign.blood_pressure_systolic,'blood_pressure_diastolic':vitalsign.blood_pressure_diastolic})
    if request.method == "POST":  
        form = VitalSignForm(request.POST, instance=vitalsign)  
        if form.is_valid():  
            try:  
                obj=form.save( commit=False) 
                obj.patient =Patient.objects.get(aadhaarId=id)
                obj.save()
                messages.success(request, 'New Vital Sign is successfully updated.!')
                # model = form.instance
                return  redirect('/patient_records/patient-detail/{}'.format(id)) 
            except:  
                messages.error(request, 'failed to update vital sign')
                
    return render(request,'patient_records/genralForm.html',{'form':form,'patient' :patient})  


def medicationStatementCreate(request,id ):
    patient= Patient.objects.get(aadhaarId=id)
    new_medication_statement = MedicationStatementForm().save(commit=False)
    try:
        print("fails")
        new_medication_statement.patient= patient
        new_medication_statement_obj=new_medication_statement.save()
        # new_medication_statement_obj = new_medication_statement.instance
        print("success")
    except:
        messages.error(request, 'failed to open new medicaiton Statement form')
        return  redirect('/patient_records/patient-detail/{}'.format(id)) 
        # model.instance
    if request.method == "POST":  
        form =MedicationItemForm( request.POST, initial={'medication_statement':new_medication_statement_obj})
        if form.is_valid():  
            try:  
                form.save()
                messages.success(request, 'New Medication statement is successfully added.!')
            except:
                messages.error(request, 'failed to Add New medicaiton Statement list')
            return  redirect('/patient_records/patient-detail/{}'.format(id))     
    else :
        form=MedicationItemForm( initial={'medication_statement':new_medication_statement_obj})
    return render(request,'patient_records/patient-medication-item.html',{'form':form,'patient' :patient})  

def eprescriptionCreate(request,id):
    patient= Patient.objects.get(aadhaarId=id)
    if request.method =="POST":
        # meditcation_statement= MedicationStatement.objects.filter(patient=patient)
        form= MedicationItemForm(request.POST)
        if form.is_valid():
            try:  
                form.save()
                messages.success(request, 'New epresciption  is successfully added.!')
            except:
                messages.error(request, 'failed to Add New E-prescription  ')
            return  redirect('/patient_records/patient-detail/{}'.format(id))     
    else :
            form=MedicationItemForm()   
    return render(request,'patient_records/genralForm.html',{'form':form,'patient' :patient})   

def patientProblemListView(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    forms= ProblemList.objects.filter(patient =patient)
    allforms=forms
    forms=[]
    for form in allforms:
        if form:
            print(form)
            print(form.problem)
            forms.append(form)
    print(forms)
    return render(request,'patient_records/patient-problem-list-view.html',{'problemLists':forms,'patient' :patient})  

def patientSocialHistoryView(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    try:
        form = SocialHistory.objects.get(patient=patient)
    except:
        return redirect(f'/patient_records/patient-social-history-create/{id}')
    return render(request,'patient_records/patient-social-history-view.html',{'form':form,'patient' :patient})

def patientVitalSignView(request , id):
    patient= Patient.objects.get(aadhaarId=id)
    try:
        form= VitalSign.objects.get(patient=patient)
    except:
        return redirect(f'/patient_records/patient-vital-sign-create/{id}')
    return render(request,'patient_records/patient-vital-sign-view.html',{'form':form,'patient' :patient})

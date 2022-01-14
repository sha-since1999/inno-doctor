from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializers import PatientSerializer
from django.contrib import messages
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

# Create your views here.
# def patientCheck(request):
#     return render(request,"patient-check.html")

def patientDetails(request):
    if request.method == "POST":  
        id= request.POST['aadhaarId']
        try:
            patient= get_object_or_404(Patient,aadhaarId=id)
            return render(request,"patient-details.html",context={'patient':patient})  
        except:
            messages.error(request, 'patient record found')
    return redirect('/patients/patient-check')  

        
def patientCheck(request):  
    patients = Patient.objects.all()  
    return render(request,"patient-check.html",{'patients':patients})  

def patientCreate(request):  
    if request.method == "POST":  
        form = PatientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                messages.success(request, 'New Patient is successfully added.!')
                model = form.instance
                return redirect('/patients/patient-check')  
            except:  
                messages.error(request, 'failed to add patient')
    else:  
        form = PatientForm()  
    return render(request,'patient-create.html',{'form':form})  

def patientUpdate(request, id):  
    patient = Patient.objects.get(aadhaarId=id)
    form = PatientForm(initial={'name': patient.name, 'aadhaarId': patient.aadhaarId, 'dob': patient.dob, 'gender': patient.gender})
    if request.method == "POST":  
        form = PatientForm(request.POST, instance=patient)  
        if form.is_valid():  
            try:  
                form.save() 
                # model = form.instance
                # messages.success(request,'patient updated!')
                return redirect('/patients/patient-check')  
            except Exception as e: 
                messages.error(request,'update error!')
    return render(request,'patient-update.html',{'form':form, 'patient':patient.aadhaarId})  




class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(Patient, aadhaarId=self.request.query_params.get("aadhaarId"))

    def get_queryset(self):
        return Patient.objects.filter().order_by('-last_udpated_on')

    def perform_destroy(self, instance):
        instance.delete()


def vitalSigns(request):
    return render(request, "vital-signs.html")
from statistics import mode
from django.db import models


# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    )
    aadhaarId          =models.CharField( primary_key=True , max_length=12 ,help_text= "patient aadhaar no | 12 digit" )
    name                  = models.CharField( max_length=20,help_text="patient aadhaar")
    date_of_birth    = models.DateField( max_length=8,help_text= "patient date of birth")
    gender               = models.CharField( choices=GENDER_CHOICES, help_text="pateint gender", max_length=1)

    
    # Patients  will be sorted using this field
    last_udpated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"
        ordering = ["-last_udpated_on"]

class ProblemList(models.Model):
    SEVERITY = (
        ("MILD", "Mild"),
        ("MODERATE", "Moderate"),
        ("SEVERE", "Severe")
    )
    # id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )
    problem = models.CharField(max_length=250, null=False, blank=False)
    body_site = models.CharField(max_length=300, null=False, blank=False)
    severity = models.CharField(max_length=20, choices = SEVERITY, default = None)
    onset_date = models.DateField(auto_now=True)
    abatement_date = models.DateField()
    diagnostic_certainty = models.CharField(max_length=200)

    


class VitalSign(models.Model):
    # id = models.IntegerField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    body_weight = models.FloatField()
    height = models.FloatField()
    respiration_rate = models.FloatField()
    pulse_rate = models.FloatField()
    body_temperature = models.FloatField()
    head_circumference = models.FloatField()
    pulse_oximetry = models.FloatField()
    body_mass_index = models.FloatField()
    blood_pressure_systolic = models.FloatField()
    blood_pressure_diastolic = models.FloatField()
    class Meta:
        verbose_name = "vitalsign"
        verbose_name_plural = "vitalsigns"

    def get_absolute_url(self):
        return reverse("vitalsign_detail", kwargs={"id": self.id})



class SocialHistory(models.Model):
    SMOKING = (
        ("NEVER_SMOKED", "Never Smoked"),
        ("CURRENT_SMOKER", "Current Smoker"),
        ("FORMER_SMOKER", "Former Smoker")
    )
    DRINKING = (
        ("NEVER_DRINKED", "Lifetime non-drinker"),
        ("CURRENT_DRINKER", "Current Drinker"),
        ("FORMER_DRINKER", "Former Drinker")
    )
    # id = models.IntegerField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    tobacco_smoking_status = models.CharField(max_length=20, choices =
    SMOKING, default = None)
    alcohol_consumption_status = models.CharField(
        max_length = 20, choices =
        DRINKING, default = None)
    alcohol_consumption_unit = models.IntegerField()
    alcohol_consumption_frequency = models.CharField(max_length=100)



class MedicationStatement(models.Model):
    # id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    description= models.TextField( null =True ,help_text="give a short description!")
    class Meta:
        verbose_name = "medicationstatement"
        verbose_name_plural = "medicationstatements"


    def get_absolute_url(self):
        return reverse("medicationstatement_detail", kwargs={"id": self.id})


class MedicationItem(models.Model):
    # id = models.IntegerField(primary_key=True)
    medication_statement = models.ForeignKey(MedicationStatement, on_delete=models.CASCADE)
    medication_item = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    form = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    unit_of_prescription = models.CharField(max_length=100, null=False, blank=False)
    batch_id = models.CharField(max_length=100, null=False, blank=False)
    expiry = models.DateField(null=False, blank=False)
    dose_amount = models.PositiveIntegerField(null=False, blank=False)
    dose_duration = models.CharField(max_length=100, null=False, blank=False)
    dose_unit = models.CharField(max_length=100, null=False, blank=False)
    dose_frequency = models.CharField(max_length=100, null=True, blank=True)
    dose_interval = models.CharField(max_length=100, null=True, blank=True)
    dose_specific_timing = models.TimeField()
    route = models.CharField(max_length=100, null=False, blank=False)
    body_site = models.CharField(max_length=100, null=False, blank=False)
   
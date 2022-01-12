from typing import Reversible
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField


# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    aadhaarId   =models.CharField( primary_key=True , max_length=16 ,help_text= "patient aadhaar" )
    name          = models.CharField( max_length=20,help_text="patient aadhaar")
    dob             = models.DateField( max_length=8,help_text= "patient date of birth")
    gender       = models.CharField( choices=GENDER_CHOICES, help_text="pateint gender", max_length=1)
    # gender      = models.TextChoices('Male', 'Female','Trans')
    
    # Patients  will be sorted using this field
    last_udpated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")
        ordering = ["-last_udpated_on"]
        app_label= 'patients'

    def __str__(self):
        return self.name 
   


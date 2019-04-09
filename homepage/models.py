from django.db import models

# Create your models here.


from django.db import models
from decimal import Decimal
TAX_RATE = Decimal("0.05")

# Create your models here.

class Doctor (models.Model):
    doctorID = models.IntegerField(default=0)
    fName = models.TextField(default="Doctor First Name")
    lName = models.TextField(default="Doctor Last Name")
    STATUS_CHOICES = [
        ( 'F', 'Female' ),
        ( 'M', 'Male' ),
    ]
    gender = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    state = models.TextField(default="Doctor Location")
    credentials = models.TextField(null = true)
    specialty = models.TextField(default="Doctor Specialty")
    OPIOID_CHOICES = [
        ( 0, 'False' ),
        ( 1, 'True' ),
    ]
    opioidPrescriber = models.IntegerField(default=OPIOID_CHOICES[0][0])
    totalPrescriptions = models.IntegerField()

class Drug (models.Model):
    drugName = models.TextField(default="Drug Name")
    STATUS_CHOICES = [
        ( 'F', 'Is Not Opiate' ),
        ( 'T', 'Is Opiate' ),
    ]
    drugType = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    
class Prescription(models.Model):
    doctorID = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    drugName = models.ForeignKey(Drug, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)

class OverdoseDeaths(models.Model):
    state = models.TextField(default="State")
    population = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    abbrev = models.ForeignKey(Doctor, on_delete=models.CASCADE)









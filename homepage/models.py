from django.db import models

# Create your models here.


from django.db import models
from decimal import Decimal
TAX_RATE = Decimal("0.05")

# Create your models here.

class Doctor (models.Model):
    firstName = models.TextField(default="Doctor First Name")
    lastName = models.TextField(default="Doctor Last Name")
    doctorID = models.IntegerField()
    STATUS_CHOICES = [
        ( 'F', 'Female' ),
        ( 'M', 'Male' ),
    ]
    gender = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    credentials = models.TextField(default="Doctor Credentials")
    location = models.TextField(default="Doctor Location")
    specialty = models.TextField(default="Doctor Specialty")
    OPIOID_CHOICES = [
        ( 'F', 'False' ),
        ( 'T', 'True' ),
    ]
    opioidPrescriber = models.CharField(max_length=1, default=OPIOID_CHOICES[0][0], choices=OPIOID_CHOICES)
    totalPrescriptions = models.IntegerField()

class Drug (models.Model):
    name = models.TextField(default="Drug Name")
    STATUS_CHOICES = [
        ( 'F', 'Is Not Opiate' ),
        ( 'T', 'Is Opiate' ),
    ]
    drugType = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    doctorID = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=6)








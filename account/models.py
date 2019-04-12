from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog import models as cmod

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)
    USER_TYPE_CHOICES = (
        (1, 'Data Clerk'),
        (2, 'Health Official'),
        (3, 'Doctor'),
    )
    user_type = models.IntegerField(null=True, choices=USER_TYPE_CHOICES)
    
    def get_shopping_cart(self):   
            # retrieve (or create) a Sale with purchased=None for this user
            cart =cmod.Sale.objects.filter(user = self, purchased = None).first()
            if cart is None:
                cart = cmod.Sale()
                cart.user = self
            cart.recalculate()
            cart.save()
            # return the Sale object
            return cart

    # retrieve (or create) a Sale with purchased=None for this user
    # return the Sale object

    #experimenting with docs found online
    #class Meta:
        #permissions= (
            #("can_search", "Ability to search data for specific user or drug"),
            #("can_view_all_prescriber_details", "Can view raw prescriber details, including names"),
            #("can_view_modified_prescriber_details", "Can view anonymized prescriber details"),
            #("can_create_data", "Can create doctor, drug, and prescription records"),
            #("can_read_data", "Can read doctor, drug, and prescription data"),
            #("can_update_data", "Can update doctor, drug, and prescription data"),
            #("can_delete_data", "Can delete doctor, drug, and prescription data"),
            #("view_all_analytics", "Can view all analytical tools"),
            #("view_select_analytics", "Can view select analytical tools"),
        #)
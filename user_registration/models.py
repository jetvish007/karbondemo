from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django_countries.fields import CountryField

class GreenUser(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    instrument_purchase = models.CharField(max_length=100, null=True)
    house_no = models.CharField(max_length=100,null=True)
    address_line1 = models.CharField(max_length=100, null=True)
    address_line2 = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=100, null=True)
    country = CountryField(blank_label='(select country)', null=True)
    creation_date = models.DateField(
        'Creation Date',
        auto_now_add = True, null=True
    )
    def __str__(self):
        return self.name

class UsageDetails(models.Model):
    """docstring for UsageDetails."""

    
    units_consumed = models.IntegerField()
    units_produced = models.IntegerField()
    units_transfered = models.IntegerField()
    creation_date = models.DateField()

    def __str__(self):
        return self.user


# Create your models here.

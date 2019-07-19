from django.db import models
from random import *
# Create your models here.

class Register(models.Model):
            
    DESIGINATION = [
        ('DGP', 'DGP'),
        ('ADGP', 'ADGP'),
        ('IGP/SIGP','IGP/SIGP'),
        ('DIGP','DIGP'),
        ('DSP','DSP'),
        ('SI','SI'),]
    p=''
    for i in range(0,4):
        p = p+str(randint(0,9))
    reg_id = models.IntegerField(default = p)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    mobile = models.CharField(max_length = 30)
    email = models.EmailField()
    designation = models.CharField(max_length = 64,choices = DESIGINATION)

    def __str__(self):
        return self.username


class Display(models.Model):
    
    title = models.CharField(max_length = 250)
    n=''
    for i in range(0,4):
        n = n+str(randint(0,9))
    eligible = models.CharField(max_length = 250)
    number_id = models.IntegerField(default = n,unique = True)
    
    def __str__(self):
        return self.title


class Fir_Details(models.Model):
    
    YEAR_IN_SCHOOL_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),]
    p = ''
    for i in range(0,4):
        p = p+str(randint(0,9))
    fir_number = models.IntegerField(default = p)
    police_station_name = models.CharField(max_length = 64)
    police_station_code = models.CharField(max_length = 10)
    police_station_city = models.CharField(max_length = 250)
    complaints_name = models.CharField(max_length = 64)
    Father_name = models.CharField(max_length = 64)
    complainants_address = models.CharField(max_length = 64)
    complainants_mobile_number = models.CharField(max_length = 15)
    place_of_loss = models.CharField(max_length = 64)
    Date = models.DateField()
    time = models.TimeField()
    case_categeory = models.CharField(max_length = 64)
    lost_articles = models.CharField(max_length = 254)
    complet_description = models.CharField(max_length = 254)
    fir_status = models.CharField(max_length = 64,choices = YEAR_IN_SCHOOL_CHOICES,default = 'active',)
    
    def __str__(self):
        return self.complaints_name




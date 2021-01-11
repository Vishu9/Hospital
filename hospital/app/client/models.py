from django.db import models
from django.contrib.auth.models import Group
from hospital.app.user.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50, unique=False) 


    class Meta:
        '''
        to set table name in database
        '''
        db_table = "Client"



class  Shift(models.Model):
#client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField() 
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    
        
    REPEAT_CHOICES = (
        ('None', 'None'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
    )
    repeat = models.CharField(max_length=20, choices=REPEAT_CHOICES)

    SHIFT_CHOICES = (
        ('Morning Shift - 5am to 9am','Morning Shift - 5am to 9am'),
    )
    
    shift_availability = models.CharField(max_length=50, choices=SHIFT_CHOICES)

   
    
    
  
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "Shift"

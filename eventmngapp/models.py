from __future__ import unicode_literals  
from django.db import models   
class Events1(models.Model):  
    Event_name = models.CharField(max_length=20)  
    Event_cost = models.IntegerField()  
    Capacity = models.IntegerField()
    Facilities= models.TextField()
    class Meta:  
        db_table = "eventmngapp_events1" 
class Bookings(models.Model): 
    Username = models.CharField(max_length=20) 
    Email_Address = models.EmailField(max_length=254) 
    Mobile_number = models.IntegerField() 
    Location  = models.CharField(max_length=20) 
    Event_name = models.CharField(max_length=20)  
    Budget = models.IntegerField()  
    Capacity = models.IntegerField()
    Facilities_Required= models.TextField()  
    class Meta:  
        db_table = "eventmngapp_Bookings" 
class EventCal(models.Model): 
    Event_name = models.CharField(max_length=20)  
    Event_date= models.DateField()
    Event_time = models.TimeField()    
    class Meta:  
        db_table = "eventmngapp_EventCal"
class Customer(models.Model):
    Customer_name = models.CharField(max_length=20)
    Query=models.TextField()

from django import forms  
from eventmngapp.models import Events1
from eventmngapp.models import Bookings
from eventmngapp.models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


  
class EventForm(forms.ModelForm):  

    class Meta:  
        model = Events1
        fields = "__all__"  
class BookingForm(forms.ModelForm):  

    class Meta:  
        model = Bookings
        fields = "__all__"  
class CustomerForm(forms.ModelForm):  

    class Meta:  
        model = Customer
        fields = "__all__" 

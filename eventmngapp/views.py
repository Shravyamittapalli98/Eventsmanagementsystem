from django.shortcuts import render, redirect,get_object_or_404
from eventmngapp.form import EventForm
from eventmngapp.form import BookingForm
from eventmngapp.form import CustomerForm


from eventmngapp.models import Events1
from eventmngapp.models import Bookings
from eventmngapp.models import Customer
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

#from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .form import CreateUserForm



# Create your views here.
def index(request):   
    return render(request,"index.html") 
def wedding(request):   
    return render(request,"wedding.html") 
def suprise(request):   
    return render(request,"suprise.html") 
def birthday(request):   
    return render(request,"birthday.html")  
def dashboard(request):
	return render(request,"dashboard.html")
def contact(request):
    return render(request,"contact.html")
def reviews(request):   
    return render(request,"reviews.html") 
def cust_reviews(request):   
    return render(request,"cust_reviews.html") 
def corporate(request):   
    return render(request,"corporate.html") 
def about(request):   
    return render(request,"about.html") 
def confirmevent(request):   
    return render(request,"confirmevent.html") 


def show_customer(request):
    ev=Events1.objects.all()
    return render(request,"show_customer.html",{'ev':ev})  

def show(request):
    ev=Events1.objects.all()
    return render(request,"show.html",{'ev':ev})  
def events1(request):
    context= {}
    form= EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/show') 

    context['form']= form  
    return render(request, "events.html", context)


def update(request, id):
    context= {}
    obj= get_object_or_404(Customer, id = id)
    form= EventForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/home") 
    context['form']= form  
    return render(request, "update.html", context)
def delete(request, id):
    context= {}
    obj= get_object_or_404(Customer, id = id)

    if request.method=="POST":
        obj.delete()
        return redirect('/home') 
    return render(request, "delete.html", context)
def upda(request, id):
    context= {}
    obj= get_object_or_404(Bookings, id= id)
    form= BookingForm(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('/user_bookings')
    context['form']= form  
    return render(request, "upda.html", context)
def dele(request, id):
    context= {}
    obj= get_object_or_404(Bookings,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('/user_bookings')
    return render(request, "dele.html", context)


def user_bookings(request):
    bk=Bookings.objects.all()
    return render(request,"user_bookings.html",{'bk':bk}) 
def bookings(request):
    context= {}
    form= BookingForm(request.POST or None)
    if form.is_valid():
        user=form.cleaned_data.get('username')
        Budget=form.cleaned_data.get('Budget')
        Capacity=form.cleaned_data.get('Capacity')
        #3cf=get_object_or_404(Bookings,Username=user)
        if Budget>5000 and Capacity<500:
            form.save()
            messages.info(request, 'Event Booked successfully')
            return redirect('/confirmevent')
        else:

            messages.info(request, 'invalid budget and capacity')
            return render(request,"customer_form.html",context)
    context['form']= form  
    return render(request, "bkngform.html", context)



def home(request):
    sc=Customer.objects.all()
    return render(request,"home.html",{'sc':sc}) 
def customer(request):
    context= {}
    form= CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard') 

    context['form']= form  
    return render(request, "customer_form.html", context)

  


def register(request):
    if  request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for'+ user)
                return redirect('login')
        context ={'form':form}
        return render(request, 'accounts/register.html', context)
def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                #login(request)
                return redirect('/dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logout(request):
    #logout(request)
    return redirect('/')

def logad(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                #login(request)
                return redirect('/home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/logad.html', context)






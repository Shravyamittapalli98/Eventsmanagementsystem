"""eventmanagementproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventmngapp import views


 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"), 
    path('logad/', views.logad, name="logad"), 
    path('logout/', views.logout, name="logout"),

    path('', views.index), 
    path('show/',views.show),

    path('events1/',views.events1),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),
    path('confirmevent/',views.confirmevent),
    
    path('customer/',views.customer),
    path('bookings/',views.bookings),
    path('user_bookings/',views.user_bookings),
    path('upda/<id>',views.upda),
    path('dele/<id>',views.dele),


    path('dashboard',views.dashboard),
    path('home/',views.home),
    path('contact/',views.contact),
    path('reviews/',views.reviews),
    path('cust_reviews/',views.cust_reviews),
    path('wedding/',views.wedding),
    path('suprise/',views.suprise),
    path('corporate/',views.corporate),
    path('birthday/',views.birthday),   
    path('about/',views.about),
]

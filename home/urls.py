from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index , name='home'),
    path("about/", views.about , name='about'),
    path("booking/", views.booking , name='booking'),
    path("contact/", views.contact , name='contact'),
    path("service/", views.service , name='service'),
    path("team/", views.team , name='team'),
    path("testimonial/", views.testimonial , name='testimonial'),
    
]
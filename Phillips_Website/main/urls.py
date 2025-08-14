from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_contact/', views.send_contact, name='send_contact'),
    path('plumbing/', views.plumbing, name='plumbing'),
    path('heating/', views.heating, name='heating'),
    path('gas/', views.gas, name='gas'),
    path('faqs/', views.faqs, name='faqs'),

]

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def send_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        service = request.POST.get('service')
        message = request.POST.get('message')

        message = f"""
        New Contact Request:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        Requested Service: {service}
        
        Message:
        {message}
        """

        send_mail(
            subject='New Contact Form Submission',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['charliewright538@gmail.com'],  # the destination inbox
            fail_silently=False,
        )

        return redirect('home')  # or render a success message page

    return redirect('home')

from django.shortcuts import render

def plumbing(request):
    return render(request, 'main/plumbing.html')


def heating(request):
    return render(request, 'main/heating.html')

def gas(request):
    return render(request, 'main/gas.html')

def faqs(request):
    return render(request, 'main/faqs.html')
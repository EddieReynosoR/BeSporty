# Create your views here.

from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import RegistrationForm
import uuid
from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy

def RegistrationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        type = request.POST.get("Type")
        address = request.POST.get("address")
        password = request.POST.get("password1")
        

        domain_name = get_current_site(request).domain
        token = str(random.random()).split('.')[1]

        user_obj = CustomUser.objects.create(username = username, email = email, address = address, auth_token = token, type = type, password = password)
        user_obj.set_password(password)
        user_obj.save()
        

        link = f'http://{domain_name}/accounts/verify/{token}'

        send_mail(
            'Email Verification',
            f'Please click {link} to verify your email!',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return HttpResponse('The mail has been sent!')

    return render(request, 'registration/signup.html', {'form': form})

def SendEmail(request):
    
    user = CustomUser.objects.get(username = request.user)
    email = user.email
    
    domain_name = get_current_site(request).domain
    token = str(random.random()).split('.')[1]
    link = f'http://{domain_name}/accounts/verify/{token}'

    send_mail(
        'Email Verification',
        f'Please click {link} to verify your email!',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return HttpResponse('The mail has been sent!')


def Verify(request, token):
    try:
        user  = CustomUser.objects.filter(auth_token = token)     
        if user:
            user.update(is_verified = True)
            # msg = 'Your email has been verified'
        return HttpResponse('Your account has been verified!') 
                
    except Exception as e:
        return render(request, 'registration/success.html', {'msg':e})



class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("token")


# class SuccessView(TemplateView):
#     template_name = "registration/success.html"

class TokenView(TemplateView):
    template_name = "registration/token.html"
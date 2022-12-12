# Create your views here.

from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
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
        return render(request, 'registration/token.html', {})

    return render(request, 'registration/signup.html', {'form': form})

def Login(request):
    

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        
        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.success(request, 'Something is wrong with the user. Check if the username or password are correct.')
            return redirect('loginForm')

        elif not user.is_verified:
            messages.success(request, 'User not verified check the email that you entered.')
            return redirect('loginForm')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html', {})

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
    return render(request, 'registration/token.html', {})


def Verify(request, token):
    try:
        user  = CustomUser.objects.filter(auth_token = token)     
        if user:
            user.update(is_verified = True)
            # msg = 'Your email has been verified'
        return render(request, 'registration/success.html', {})
                
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
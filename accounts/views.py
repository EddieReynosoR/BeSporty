# Create your views here.

from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import RegistrationForm, CustomUserChangeForm
from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy

def RegistrationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            address = request.POST.get("address")
            password = request.POST.get("password1")
            
        
            domain_name = get_current_site(request).domain
            token = str(random.random()).split('.')[1]

            user_obj = CustomUser.objects.create(username = username, email = email, address = address, auth_token = token, password = password)
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
        except:
            messages.success(request, 'Something went wrong with the registration. Try again.')
            return redirect('registration')


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

def EditProfileView(request):
    form = CustomUserChangeForm()
    if request.method == 'POST':
        username = request.POST.get("username")
        print(username)
        email = request.POST.get("email")
        address = request.POST.get("address")
        
        
        if username is not None and email is not None and address is not None:
            if request.user.is_authenticated:
                user = request.user

                if username != user.username or email != user.email or address != user.address:
                    if CustomUser.objects.filter(username=username).exclude(id=user.id).exists():
                        messages.success(request, 'Username already in use.')
                        return redirect('edit')
                    elif CustomUser.objects.filter(email=email).exclude(id=user.id).exists():
                        messages.success(request, 'Email already in use.')
                        return redirect('edit')
                    else:
                        
                        user_obj=CustomUser.objects.get(id = user.id)


                        if user_obj.email != email:
                            user_obj.is_verified = False
                            
                            user_obj.username = username
                            user_obj.email = email                          
                            user_obj.address = address

                            

                            
                            user_obj.save()
                            messages.success(request, 'Your data has been changed. Your email has been changed, check your new email and verify it.')
                            

                            token = user_obj.auth_token

                            domain_name = get_current_site(request).domain
                            

                            link = f'http://{domain_name}/accounts/verify/{token}'

                            send_mail(
                                'Email changed',
                                f'Please click {link} to verify your new email!',
                                settings.EMAIL_HOST_USER,
                                [email],
                                fail_silently=False,
                            )
                            logout(request)
                            return redirect("loginForm")
                        else:

                            user_obj.username = username
                            user_obj.email = email                         
                            user_obj.address = address

                            

                            
                            user_obj.save()
                            logout(request)
                            messages.success(request, 'Your data has been changed.')
                            
                            
                            return redirect("loginForm")
                else:
                    messages.success(request, 'You already have the same information.')
                    return redirect("edit")
        else:
            messages.success(request, 'Null data not allowed')
            return redirect("edit")

            
                
        

    return render(request, 'registration/edit_profile.html', {'form': form})

def PasswordReset(request):
    if request.method == 'POST':
        email = request.POST.get("email")

        if not CustomUser.objects.filter(email = email):
            messages.success(request, 'The email is not registered.')
            return redirect("resetpassword")
        else:
            user_obj = CustomUser.objects.filter(email = email).get()
            token = user_obj.auth_token

            domain_name = get_current_site(request).domain
            

            link = f'http://{domain_name}/accounts/passwordChange/{token}'

            send_mail(
                'Reset password',
                f'Please click {link} to proceed with your password change.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'registration/token3.html', {})

        
    return render(request, 'registration/password_reset_form.html', {})


def PasswordChange(request, token):
    if request.method == 'POST':
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")
        
        if new_password1 is not None or new_password2 is not None:
            user_obj = CustomUser.objects.filter(auth_token = token).get()
            # if old_password == user_obj.password:
            if new_password1 != new_password2:
                messages.success(request, 'Please confirm your password.')
                return redirect("changepassword", token = token)    
            else:
                user_obj.set_password(new_password1)
                user_obj.save()

                return redirect("loginForm")
            # else:
            #     messages.success(request, 'Your old password is not correct.')
            #     return redirect("changepassword", token = token)
        else:
            messages.success(request, 'Null data not allowed.')
            return redirect("changepassword", token = token)
    return render(request, 'registration/password_change_form.html', {})

        
   
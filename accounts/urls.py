from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationView, name='registration' ),
    path('verify/<str:token>', views.Verify),
    path('sendEmail/', views.SendEmail, name='sendEmail' ),
    path('loginForm/', views.Login, name='loginForm'),
    path('editProfile/', views.EditProfileView, name='edit'),
    path('resetPassword/', views.PasswordReset, name='resetpassword'),
    path('passwordChange/<str:token>', views.PasswordChange, name='changepassword')
]
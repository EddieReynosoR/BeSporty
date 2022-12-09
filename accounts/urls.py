from django.urls import path
from . import views
from .views import SignUpView, TokenView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('registration/', views.RegistrationView, name='registration' ),
    path('verifyEmail/', TokenView.as_view(), name='token'),
    path('verify/<str:token>', views.Verify),
    path('sendEmail/', views.SendEmail, name='sendEmail' ),
]
# Create your views here.

from django.views.generic.edit import CreateView
from .forms import RegistrationForm

from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
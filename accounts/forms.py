from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= CustomUser
        fields =  UserChangeForm.Meta.fields
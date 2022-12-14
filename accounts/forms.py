from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["password1"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["password2"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["username"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["address"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["email"].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('address', 'email')

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["password"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["username"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["address"].widget.attrs.update({
            'class':'form-control',
        })
        self.fields["email"].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
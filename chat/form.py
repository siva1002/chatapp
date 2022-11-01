from pydoc import ModuleScanner
from attr import fields
from django import forms
from .models import *
from django.forms import CharField, Form, PasswordInput
from  django.contrib.auth.models import User
class room(forms.ModelForm):
    class Meta:
        model=room
        fields='__all__'
class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password =forms. CharField(widget=PasswordInput())
class signupform(forms.ModelForm):
    
    def save(self, commit=True):
       # Save the provided password in hashed format
       user = super().save(commit=False)
       print(user)
       user.set_password(self.cleaned_data["password"])
       if commit:
        user.save()
        return user
    class Meta:
        model=User
        fields=['username','email','password']
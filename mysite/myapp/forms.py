
from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount','category')
        
        
        
class CreateUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email' ,'password1', 'password2')
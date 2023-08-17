from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
import datetime
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForms  
from django.contrib.auth.decorators import login_required

# Create your views here.
login_required(login_url='login')
#Function to add the expenses
login_required(login_url='login')
def index(request):
    if request.method =="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
            
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
   
    #Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))
    
    #for daily sum of the expenses according to the date 
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    
    #for categorical sum of the expenses according to the category 
    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    
    
    expense_form = ExpenseForm()
    return render(request,'myapp/index.html',{'expense_form':expense_form,'expenses':expenses, 'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})

#Function to edit the expenses
def edit(request,id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    
    if request.method =="POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request,'myapp/edit.html',{'expense_form':expense_form})


#Function to delete the expenses
def delete(request,id):
    if request.method =="POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
        
    return redirect('index')
   







  # Import your custom form
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib import messages

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Authenticate and login the user
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('login')  # Redirect to the login page
#             else:
#                 messages.error(request, 'Authentication failed. Please check your credentials.')
#         else:
#             messages.error(request, 'Error occurred during signup. Please check the form.')
#     else:
#         form = CustomUserCreationForm()  # Use the custom form here
#     return render(request, 'myapp/signup.html', {'form': form})


def registerpage(request):
    form=CreateUserForms()
    if request.method=="POST":
        form=CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')
    context={"form":form}
    return render(request,'myapp/signup.html',context)

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if  user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'myapp/login.html')
    context={}
    return render(request,'myapp/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def tryd(request):
    
            
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
   
    #Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))
    
    #for daily sum of the expenses according to the date 
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    
    #for categorical sum of the expenses according to the category 
    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    
    
    expense_form = ExpenseForm()
    return render(request,'myapp/try.html',{'expense_form':expense_form,'expenses':expenses, 'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})


def try1(request):
    
            
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
   
    #Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
    #Logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))
    
    #for daily sum of the expenses according to the date 
    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    
    #for categorical sum of the expenses according to the category 
    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    
    
    expense_form = ExpenseForm()
    return render(request,'myapp/try1.html',{'expense_form':expense_form,'expenses':expenses, 'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})

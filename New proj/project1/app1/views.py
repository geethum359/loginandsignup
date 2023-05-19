from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from app1.forms import CustomUserCreationForm
from app1.models import CustomUser
from django.http import HttpResponse
from app1.forms import employeeForm
from django.contrib.auth import authenticate,login,logout
from app1.models import employee
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')

def signup1(request):
    form=CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup1.html',{"form":form})
def user_login1(request):
    if(request.method=="POST"):
        name = request.POST['n']
        password = request.POST['p']
        user =authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('invalid ... no user found')
    return render(request,'login1.html')
def user_logout1(request):
    logout(request)
    return user_login1(request)
def view(request):
    v=employee.objects.all()
    return render(request,'view.html',{"s":v})
def  addform(request):
    form=employeeForm()
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return view(request)
    return render(request,'addform.html',{'form':form})
def delete_emp(request,p):
    s=employee.objects.get(pk=p)
    s.delete()
    return view(request)
def edit_emp(request,p):
    d=employee.objects.get(pk=p)
    form=employeeForm(instance=d)
    if(request.method=='POST'):
        form=employeeForm(request.POST,instance=d)
        if(form.is_valid()):
            form.save()
            return view(request)
    return render(request,'addform.html',{'form':form})
def data(request,p):
    k=employee.objects.get(pk=p)
    form=employeeForm(instance=d)
    if(request.method=='POST'):
        form=employeeForm(request.POST,instance=d)
        if(form.is_valid()):
            form.save()
            return data(request)
    return render(request,'view_data.html')


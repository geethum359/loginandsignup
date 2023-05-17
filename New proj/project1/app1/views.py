from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from app1.forms import CustomUserCreationForm
from app1.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# from app1.models import employee
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
# def view(request):
#     v=employee.objects.all()
#     return render(request,'view.html',{"s":v})
# def  addform(request):
#     if(request.method=='POST'):
#         eid=request.POST['eid']
#         n=request.POST['en']
#         p=request.POST['ep']
#         # g1=request.POST['g1']
#         # g2=request.POST['g2']
#         cn=request.POST['cn']
#         d=request.POST['d']
#         s=request.POST['s']
#         o=employee.objects.create(emp_id=eid,emp_name=n, place=p,company_name=cn,designation=d, salary=s)
#         o.save()
#         return view(request)
#     return render(request,'addform.html')

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .forms import UserRegister
# Create your views here.
from .models import *
def home(request):
    emp=Emp.objects.all()
    
    if request.GET.get('search'):
        search=request.GET.get('search')
        emp=emp.filter(emp_name__icontains=search)
    return render(request,'emp/home.html',{'emp':emp})
@login_required(login_url='loggedin')
def add_emp(request):
    if request.method=='POST':
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        emp_phone=request.POST.get('emp_phone')
        emp_address=request.POST.get('emp_address')
        emp_is_active=request.POST.get('emp_is_active')
        emp_department=request.POST.get('emp_department')
        
        e=Emp.objects.create(
            emp_name=emp_name,
            emp_id=emp_id,
            emp_phone=emp_phone,
            emp_address=emp_address,
            emp_department=emp_department,
            
            
            
        )
        if emp_is_active is None:
            e.emp_is_active=False
        else:
            e.emp_is_active=True
        
        e.save()
        return redirect('home')
            
    return render(request,'emp/add_emp.html')

@login_required(login_url='loggedin')
def del_emp(request,id):
    e=get_object_or_404(Emp,id=id)
    # print(e.id)
    
    e.delete()
    return redirect('home')

@login_required(login_url='loggedin')
def update_emp(request,id):
    e=get_object_or_404(Emp,id=id)
    if request.method=='POST':
        emp_name=request.POST.get('emp_name')
        emp_id=request.POST.get('emp_id')
        emp_phone=request.POST.get('emp_phone')
        emp_address=request.POST.get('emp_address')
        emp_is_active=request.POST.get('emp_is_active')
        emp_department=request.POST.get('emp_department')
        
        
        e.emp_name=emp_name
        e.emp_id=int(emp_id)
        e.emp_phone=emp_phone
        e.emp_address=emp_address
        e.emp_department=emp_department
            
            
            
        
        if emp_is_active is None:
            e.emp_is_active=False
        else:
            e.emp_is_active=True
        
        e.save()
        return redirect('home')
        
    
    return render(request,'emp/update_emp.html',{'e':e})
    
@login_required(login_url='loggedin')  
def testimonial(request):
    testi=Testimonial.objects.all()
    if request.GET.get('search'):
        s=request.GET.get('search')
        testi=testi.filter(name__icontains=s)
        
    return render(request,'emp/testimonial.html',{'testi':testi})
    
def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()
            login(request,form)
            return redirect('home')
        else:
            return render(request,'emp/register.html' ,{'form':form})
            
            
    form=UserRegister()
    return render(request,'emp/register.html' ,{'form':form})

def loggedin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=AuthenticationForm()
        return render(request,'emp/login.html',{'form':form})
    
def loggedout(request):
    logout(request)
    return redirect('home')
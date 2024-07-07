from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms  import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render (request, 'accounts/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,'POST')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('Admindashboard')
            elif  user is not None and user.is_doctor:
                login(request,user)
                return redirect('Doctordashboard')
            elif user is not None and user.is_receptionist:
                login(request,user)
                return redirect('Receptionistdashboard')
            elif user is not None and user.is_lab_technician:
                login(request,user)
                return redirect('Labtechniciandashboard')
            elif user is not None and user.is_accountant:
                login(request,user)
                return redirect('Accountantdashboard')
            else:
                 messages.error(request,'Invalid Credentials') 
        else:
            messages.info(request,'error validating form') 
    return render(request, 'login.html',{'form':form})                  

def logout_view(request):
    logout(request)
    return redirect('index')

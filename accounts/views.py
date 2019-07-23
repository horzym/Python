from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That emial is in database')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    #auth.login(request,user)
                    #messages.success(request,'Success login!')
                    #return redirect('index')
                    user.save()
                    messages.success(request,'You are registered!')
                    return redirect('login')

        else:
            messages.error(request,'Password not match')
            return redirect('register')


        return redirect('register')
    else:
        return render(request,'accounts/register.htm')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged in!')
            return redirect('dashboard')
        else:
            messages.error(request,'User not exist...')
            return redirect('register')
    else:
        return render(request,'accounts/login.htm')

def logout(request):
    auth.logout(request)
    messages.success(request,'You are logout, bye!')
    return redirect('index')

def dashboard(request):
    
    return render(request,'accounts/dashboard.htm')
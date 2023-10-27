from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        name=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        mail=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['password1']
        if passw == cpass:
            if User.objects.filter(username=name).exists():
                messages.info(request,"username taken")
                return redirect("register")
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,password=passw,first_name=fname,last_name=lname,email=mail)

            user.save();
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
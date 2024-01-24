from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmPassword')
        
        # Check if passwords match before creating the user
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"password does not match")
            return redirect('register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request,"invalid username or password")
                return render(request, 'login')
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')



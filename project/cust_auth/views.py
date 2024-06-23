from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout



def register_view(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            name = request.POST.get('name')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if not email or not name or not password1 or not password2:
                messages.error(request, "Email, password is required !")
                return redirect('register')

            if password1 != password2:
                messages.error(request, "password does not match !")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "account already exit with this email !")
                return redirect('register')
            

            user = User(
                email = email,
                name = name,
                password = make_password(password1)
            )

            user.save()
            messages.success(request, "Registration successful !")
            return redirect('/login')
        else:
            return render(request, 'register.html')
    except:
        return render(request, 'register.html')
    

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/dashboard')
    try:
    
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request, "invalid credential !")
                return render(request, 'login.html')
        else:
            messages.error(request, "invalid credential !")
            return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def logout_view(request):
    try:
        logout(request)
        return redirect('/login')
    except:
        return redirect('/login')
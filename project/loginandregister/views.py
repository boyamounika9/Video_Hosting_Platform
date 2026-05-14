from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # PASSWORD CHECK
        if password != cpassword:

            messages.error(request, 'Passwords are not matching')

            return render(request, 'register.html')

        # USER EXISTS
        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists')

            return render(request, 'register.html')

        # CREATE USER
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Registration Successful. Login Now')

        return redirect('login')

    return render(request, 'register.html')

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, 'Login Successful')

            return redirect('home')

        else:

            messages.error(request, 'Invalid Username or Password')

            return render(request, 'login.html')

    return render(request, 'login.html')

# LOGOUT

def logout_view(request):

    logout(request)

    messages.success(request, 'Logout Successful')

    return redirect('login')
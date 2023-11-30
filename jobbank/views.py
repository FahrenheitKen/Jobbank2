from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import CustomUser


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def jobs(request):
    return render(request, 'job-list.html')


def contacts(request):
    return render(request, 'contact.html')


def Terms_Condition(request):
    return render(request, 'T&C.html')


def error(request):
    return render(request, '404.html')


def login_signup(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        # Retrieve data from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Perform basic form validation
        if not (email and password):
            messages.error(request, 'Email and password are required.')
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Replace 'dashboard' with the actual URL name of your dashboard page
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Perform basic form validation
        if not (first_name and last_name and email and password and confirm_password):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check if the user with the given email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,  # Using email as the username, you can change it based on your model
            password=password,
        )

        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('login')  # Replace 'login' with the actual URL name of your login page

    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'jobseeker_dashbord.html')

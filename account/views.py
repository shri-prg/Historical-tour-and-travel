from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile  # If using a Profile model

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            
            storage = messages.get_messages(request)
            for _ in storage:
                pass  
            return redirect('/')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('register')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different email.")
            return redirect('register')

        # Validate contact number length (only if provided)
        if contact_number and not (10 <= len(contact_number) <= 15):
            messages.error(request, "Contact number must be between 10 and 15 digits.")
            return redirect('register')

        # Validate passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Create the user and hash the password
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password1)  # Hash the password
        user.save()

        # Update the profile's contact number (if provided)
        if contact_number:
            user.profile.contact_number = contact_number
            user.profile.save()

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'register.html')

# Define the logout function
def logout(request):
    auth_logout(request)  # Use Django's built-in logout function
    messages.success(request, "You have successfully logged out!")
    return redirect('/')
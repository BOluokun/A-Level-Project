from django.shortcuts import render, redirect
from .pythonSubroutines import *


# Create your views here.

def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        if check_details(username, password):
            return redirect('user_library', username = username)
        else:
            message = "The details you have entered are incorrect. Please try again."
            return render(request, 'accounts/login.html', {'message': message})
    except KeyError:
        return render(request, 'accounts/login.html', {'message' : 'None'})

def create_account(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if validate_details(email, password1):
                user = make_record(username, email, password1)
                return redirect('user_library', username = user.username)
            else:
                message = """Invaild email or password entered.
                Password must be at least 8 characters long and contain at least one lowercase letter, uppercase letter, digit and special character.
                Special characters that are allowed are: @, !, £, %, ^, &, *, (, ), -, _, =, +, ?, [, ], { and }."""
                return render(request, 'accounts/create_account.html', {'message': message})
        else:
            message = "The passwords entered do not match."
            return render(request, 'accounts/create_account.html', {'message': message})
    except KeyError:
        return render(request, 'accounts/create_account.html', {'message': 'None'})

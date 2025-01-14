from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required







def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!")
            return redirect('login')
        
    return render(request, 'login.html')

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_confirm')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password are not the same!")
            return redirect('signup')
        
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

@login_required
def home(request):
    return render(request, 'home.html')



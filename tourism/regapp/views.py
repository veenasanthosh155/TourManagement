from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":  # After submission
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fname = request.POST['f']
        lname = request.POST['l']
        e = request.POST['e']
        if p == cp:
            user = User.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=e)
            user.save()
            return redirect('tourapp:home')
        else:
            return HttpResponse("Passwords are not the same")
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('tourapp:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('regapp:register')

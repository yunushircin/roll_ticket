from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Kullanıcı adı ya da şifre hatalı')

    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    context = {}
    return render(request, 'base/dashboard.html', context)

def userPage(request):
    context = {}
    return render(request, 'base/user.html', context)


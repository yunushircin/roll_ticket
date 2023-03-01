from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

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

@unauthenticated_user
def addUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, username + 'için hesap oluşturuldu')

            return redirect('home')
    context = {'form':form}
    return render(request, 'base/addUser.html', context)



@login_required(login_url='login')
@admin_only
def home(request):
    problems = Problem.objects.all()
    callcenters = CallCenter.objects.all()

    total_callcenters = callcenters.count()
    total_problems = problems.count()
    open = problems.filter(status='Açık').count()
    close = problems.filter(status='Kapalı').count()

    context = {'problems':problems, 'callcenters':callcenters, 'total_callcenters':total_callcenters,'total_problems':total_problems,'open':open,'close':close}

    return render(request, 'base/dashboard.html', context)

def userPage(request):
    context = {}
    return render(request, 'base/user.html', context)

def category(request):
    categories = Category.objects.all()
    context = {'categories' : categories}

    return render(request, 'base/category.html', context)

def callCenter(request, pk_test):
    callcenter = CallCenter.objects.get(id=pk_test)

    problems = callcenter.problem_set.all()
    problem_count = problems.count()

    context = {'callcenter':callcenter, 'problems':problems, 'problem_count':problem_count}
    return render(request, 'base/callcenter.html', context)


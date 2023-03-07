from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProblemForm, CategoryForm, AddUserForm
from .filters import ProblemFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

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

def allUser(request):
    users = User.objects.all()
    form = AddUserForm()

    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, username + ' için hesap oluşturuldu')

            return redirect('alluser')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context = {'users':users, 'form':form}

    return render(request, 'base/alluser.html', context)



@login_required(login_url='login')
@admin_only
def home(request):
    problems = Problem.objects.all()
    users = User.objects.all()

    total_users = users.count()
    total_problems = problems.count()
    open = problems.filter(status='Açık').count()
    close = problems.filter(status='Kapalı').count()

    problem_filter = ProblemFilter(request.GET, queryset=problems)
    problems = problem_filter.qs

    context = {'problems':problems, 'users':users, 'total_users':total_users,'total_problems':total_problems,'open':open,'close':close, 'problem_filter':problem_filter}

    return render(request, 'base/dashboard.html', context)

def userPage(request):
    user = request.user
    problems = user.problem_set.all()
    form = ProblemForm()

    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')

    context = {'problems':problems, 'user':user, 'form':form}
    return render(request, 'base/user.html', context)

def category(request):
    categories = Category.objects.all()
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Yeni kategori açıldı')
            return redirect('category')

    context = {'categories' : categories, 'form':form}

    return render(request, 'base/category.html', context)

def deleteCategory(request ,pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category')

    context= {'item':category}
    return render(request, 'base/delete_category.html', context)

def updateProblem(request,pk):
    problem = Problem.objects.get(id=pk)
    form = ProblemForm(instance=problem)

    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'base/update_problem.html', context)





from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm

def index (request):
    return render(request,'DEMOAPP/index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been Loged in !'))
            return redirect('index')

        else:
            messages.success(request,('Error Login !'))
            return redirect('login')
    else:
        return render(request,'DEMOAPP/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged Out!'))
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Completed'))
            return redirect('index')

    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'DEMOAPP/register.html', context)



""" def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Completed'))
            return redirect('index')

    else:
        form = UserCreationForm()
    context={'form':form}
    return render(request,'DEMOAPP/register.html',context)"""


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have edited your profile'))
            return redirect('index')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'DEMOAPP/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('You have change your password'))
            return redirect('index')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'DEMOAPP/change_password.html', context)


def courts(request):
    return render(request,'DEMOAPP/courts.html')
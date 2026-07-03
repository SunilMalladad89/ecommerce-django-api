from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import RegisterForm

# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('products:product-list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created  for {username}! Please Login.')
            return redirect('users:login')
        
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# LOGIN VIEW
def login_view(request):
    if request.user.is_authenticated:
        return redirect('products:product-list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('products:product-list')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'users/login.html')


# Logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('users:login')
    return redirect('products:product-list')
        
        

# PROFILE VIEW
@login_required(login_url='users:login')
def profile_view(request):
    return render(request, 'users/profile.html')
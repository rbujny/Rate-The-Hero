from django.shortcuts import render, redirect
from .forms import RegisterUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = RegisterUserFrom()
        context = {"form": form}
        if request.method == "POST":
            form = RegisterUserFrom(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account has been created")
                return redirect("login")

        return render(request, 'Users/register.html', context)


def loginP(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or password is incorrect.")
            return render(request, 'Users/login.html',)
    return render(request, 'Users/login.html')

def logoutU(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def myProfile(request, username):
    return render(request, 'Users/myprofile.html')

@login_required(login_url="login")
def delete(request):
    return redirect('index')

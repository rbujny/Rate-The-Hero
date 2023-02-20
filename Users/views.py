from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import RegisterUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Reviews.models import Review
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
    if username == request.user.username:
        review_list = Review.objects.filter(name=username)
        p = Paginator(review_list, 10)
        page = request.GET.get('page')
        reviews = p.get_page(page)

        if request.method == "POST":
            for review in reviews:
                hero = review.hero.get()
                hero.quantity -= review.rating
                hero.numbers -= 1
                review.delete()
                hero.save()
            user = User.objects.get(username=username)
            user.delete()
            return redirect('index')
        context = {
            "username": username,
            "reviews": reviews,
            "counter": review_list.count()
        }
        return render(request, 'Users/myprofile.html', context)
    else:
        return render(request, "Users/notYourProfile.html", {
            'username': request.user.username
        })

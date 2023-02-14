from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'Reviews/index.html')


def universe(request, uni):
    return render(request, "Reviews/universe.html")


def hero(request, hero):
    return render(request, "Reviews/hero.html")

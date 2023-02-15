from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Universe, Hero
# Create your views here.





def index(request):
    universal = Universe.objects.all()
    heroes = Hero.objects.all()
    bestRated = []
    for hero in heroes:
        if hero.numbers != 0:
            avg = hero.quantity/hero.numbers
        else:
            avg = 0
            bestRated.append({
                "name" : hero.name,
                "img": hero.img,
                "avg": avg
            })
    sorted(bestRated, key=lambda x: x["avg"])
    context = {"username": '',
               "universal": universal,
               "mostRated": heroes.order_by("numbers")[:5],
               "bestRated": bestRated,
               "reviews": ''}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'Reviews/index.html', context)


def universe(request, uni):
    universe = Universe.objects.get(slug=uni)
    heroes = Hero.objects.all().filter(universe=universe)
    return render(request, "Reviews/universe.html", {
        "heroes": heroes})


def hero(request, hero):
    return render(request, "Reviews/hero.html")


def review(request, rev_id):
    return render(request, 'Reviews/base.html')


def heroReview(request, hero_id):
    return render(request, 'Reviews/base.html')

@login_required(login_url="login")
def addRev(request):
    return render(request, 'Reviews/base.html')
@login_required(login_url="login")
def editRev(request, rev_id):
    return render(request, 'Reviews/base.html')
@login_required(login_url="login")
def delRev(request, rev_id):
    return render(request, 'Reviews/base.html')
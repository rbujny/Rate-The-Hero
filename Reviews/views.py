from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Universe, Hero, Review
from .forms import ReviewForm, SearchForm
from django.contrib import messages


# Create your views here.


def index(request):
    universal = Universe.objects.all()
    heroes = Hero.objects.all()
    bestRated = []
    for hero in heroes:
        if hero.numbers != 0:
            avg = hero.quantity / hero.numbers
        else:
            avg = 0
        bestRated.append({
            "name": hero.name,
            "img": hero.img,
            "avg": avg,
            "id": hero.id
        })
    bestRated = sorted(bestRated, key=lambda x: x["avg"], reverse=True)[:5]
    context = {"username": '',
               "universal": universal,
               "mostRated": heroes.order_by("-numbers")[:5],
               "bestRated": bestRated,
               "reviews": ''}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'Reviews/index.html', context)


def universe(request, uni):
    universe = Universe.objects.get(slug=uni)
    heroes = Hero.objects.all().filter(universe=universe)
    avg = {}
    for hero in heroes:
        hero.avg = hero.quantity/hero.numbers
    return render(request, "Reviews/universe.html", {
        "universe": universe.name,
        "heroes": heroes})


def hero(request, hero):
    selected_hero = Hero.objects.get(id=hero)
    selected_hero.avg = selected_hero.quantity/selected_hero.numbers
    last_reviews = Review.objects.filter(hero=selected_hero)[:5]
    best_reviews = Review.objects.filter(hero=selected_hero).order_by('-rating')[:5]
    return render(request, "Reviews/hero.html", {
        "hero": selected_hero,
        "best_reviews": best_reviews,
        "last_reviews": last_reviews,
    })


def review(request, rev_id):
    rev = Review.objects.get(id=rev_id)
    hero = rev.hero.get()
    if request.method == "POST":
        hero.quantity -= rev.rating
        hero.numbers -= 1
        rev.delete()
        hero.save()
        messages.success(request, "Review has been deleted.")
        return redirect('myProfile', request.user.username)
    context = {"review" : rev,"username":request.user.username}
    return render(request, 'Reviews/revs/review.html', context)


def search(request):
    form = SearchForm()
    if request.method == "POST":
        sForm = SearchForm(request.POST)
        if sForm.is_valid():
            heroes = Hero.objects.filter(
                Q(name__icontains=sForm.cleaned_data["name"])
            )[:10]
            return render(request, 'Reviews/search/search.html', {
                "form": form,
                "heroes": heroes,
                "method": "POST"
            })
    return render(request, 'Reviews/search/search.html', {
        "form": form,
    })

@login_required(login_url="login")
def addRev(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    user = request.user
    form = ReviewForm()
    if request.method == "POST":
        if Review.objects.filter(hero=hero, name=user).exists():
            messages.info(request, "You already added review to this hero.")
            return redirect("myProfile", username=request.user.username)
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            review = Review.objects.create(
                name=request.user.username,
                rating=rev_form.cleaned_data['rating'],
                text=rev_form.cleaned_data['text'],
            )
            hero.quantity += rev_form.cleaned_data['rating']
            hero.numbers += 1
            review.save()
            review.hero.add(hero)
            hero.save()
            messages.success(request, "Review has been added")
            return redirect("myProfile", username=request.user.username)
    context = {
        "hero": hero,
        "user": user,
        "form": form
    }
    return render(request, 'Reviews/revs/addrev.html', context)

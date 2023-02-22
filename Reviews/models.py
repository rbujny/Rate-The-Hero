from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Universe(models.Model):
    class Meta:
        verbose_name_plural = "Universes"

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}"


class Hero(models.Model):
    class Meta:
        verbose_name_plural = "Heroes"

    name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    superpowers = models.TextField()
    desc = models.TextField()
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    # review = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    numbers = models.IntegerField(default=0)

    def __str__(self):
        if self.numbers != 0:
            return f"{self.name}"
        else:
            return f"{self.name}"


class Review(models.Model):
    name = models.CharField(max_length=50)
    rating = models.FloatField(default=1, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    text = models.TextField()
    hero = models.ManyToManyField(Hero, blank=False)

    def __str__(self):
        return f"{self.name} rated {self.rating}"

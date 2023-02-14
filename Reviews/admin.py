from django.contrib import admin
from .models import Universe, Review, Hero

# Register your models here.

class UniverseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Universe, UniverseAdmin)
admin.site.register(Review)
admin.site.register(Hero)
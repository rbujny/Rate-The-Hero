from django.contrib import admin
from .models import Universe, Review, Hero


# Register your models here.

class UniverseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ReviewAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class HeroAdmin(admin.ModelAdmin):
    fields = ("name", "real_name", "img", "superpowers",
              "desc", "universe")

admin.site.register(Universe, UniverseAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Hero, HeroAdmin)

from django.urls import path
from . import views

urlpatterns = [
    path('<int:review_id>', views.review, name="rev"),
    path('hero/<int:hero_id>', views.heroReview, name="heroRev"),
    path ('add', views.addRev, name="addRev"),
    path ('<int:review_id>/edit', views.editRev, name="editRev"),
    path ('<int:review_id>/delete', views.delRev, name="deleteRev"),
]
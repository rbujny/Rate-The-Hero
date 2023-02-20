from django.urls import path
from . import views

urlpatterns = [
    path('<int:rev_id>', views.review, name="rev"),
    path ('add/<int:hero_id>', views.addRev, name="addRev"),
    # path ('delete/<int:rev_id>', views.delRev, name="deleteRev"),
]
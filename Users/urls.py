from django.urls import path
from . import views

urlpatterns = [
    path ('login', views.loginP, name="login"),
    path ('logout', views.logoutU, name="logout"),
    path ('register', views.register, name="register"),
    path ('myprofile/<slug:username>', views.myProfile, name="myProfile"),
    # path ('delete', views.delete, name="delete"),
]
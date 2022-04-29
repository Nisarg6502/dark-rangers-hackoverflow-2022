from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="website"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("product/", views.product, name="product"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.contact, name="contact"),
    path("signuppage/", views.signuppage, name="signuppage"),
    path("signup/", views.signup, name="signup"),
]
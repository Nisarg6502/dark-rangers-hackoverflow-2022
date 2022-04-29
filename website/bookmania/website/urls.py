from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="website"),
    path("dashboard/", views.dashboard, name="website"),
    path("product/", views.product, name="website"),
    path("profile/", views.profile, name="website"),
    path("contact/", views.contact, name="website"),
]

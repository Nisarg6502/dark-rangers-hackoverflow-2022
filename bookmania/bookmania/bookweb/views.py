from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser


# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def signuppage(request):
    return render(request, 'signup.html')

def signup(request):
    message = False
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        contact = request.POST.get('contact', '')
        age = request.POST.get('age', '')
        address = request.POST.get('address', '')

        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name, contact=contact,  age=age, address=address)
        messages.success(request, 'Your Kronos account has been successfully created!')
        user.save()
    return redirect('website')
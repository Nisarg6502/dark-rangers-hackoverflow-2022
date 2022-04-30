from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser, Contact, Book


# Create your views here.
def index(request):
    allBooks = []
    catprods = Book.objects.values('book_name')
    # print(catprods)
    cats = {item['book_name'] for item in catprods}
    print(cats)
    for cat in cats:
        # print(cat)
        book = Book.objects.filter(book_name=cat)
        # print(book)
        n = len(book)
        # print(n)
        if (n % 2 == 0):
            outer = int(n / 2)
            # print(outer)
        else:
            outer = n // 2 + 1

    allBooks.append([cats, range(len(cats)), range(n), book])

    # allProds = Product.objects.all()
    # print(allProds)
    print(allBooks)
    params = {'allBooks': allBooks}

    return render(request, 'index.html', params)

def dashboard(request):

    if request.method == "POST":
        book_name = request.POST.get('book_name', '')
        image = request.POST.get('image', '')
        author = request.POST.get('author', '')
        publishing_house = request.POST.get('publishing_house', '')
        ISBN_number = request.POST.get('ISBN_number', '')
        availability = request.POST.get('availability')
        description = request.POST.get('description')
        provider = request.user
        # provider = current_user.username
        book = Book(provider=provider, book_name=book_name, image=image, author=author, publishing_house=publishing_house, ISBN_number=ISBN_number, availability=availability, description=description)
        book.save()

    allBooks = []
    provider = request.user.id
    print(provider)
    Userprods = Book.objects.values('provider')
    # print(Userprods)
    cats = {item['provider'] for item in Userprods}
    print(cats)


    for cat in cats:
        # print(cat)
        if (cat == request.user.id):
            print(request.user.id)
            book = Book.objects.filter(provider=cat)
            print(book)

            n = len(book)
            # print(n)
            if (n % 2 == 0):
                outer = int(n / 2)
                # print(outer)
            else:
                outer = n // 2 + 1
            allBooks.append([range(outer), range(n), book])

            # allProds = Product.objects.all()
            # print(allProds)
            params = {'allBooks': allBooks}

            return render(request, 'dashboard.html', params)
        else:
            continue
            return render(request, 'dashboard.html')



def profile(request):
    return render(request, 'profile.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, subject=subject, query=query)
        contact.save()
        thank = True

    return render(request, 'contact.html', {'thank': thank})

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

def logoutUser(request):
    logout(request)
    print("Logged out")
    return redirect('website')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            print("success login")
            return redirect('website')
        else:
            messages.error(request, "Error login")
            print("Error login")
            return redirect('website')

def postbook(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name', '')
        image = request.POST.get('image', '')
        author = request.POST.get('author', '')
        publishing_house = request.POST.get('publishing_house', '')
        ISBN_number = request.POST.get('ISBN_number', '')
        availability = request.POST.get('availability')
        description = request.POST.get('description')
        provider = request.user
        # provider = current_user.username
        book = Book(provider=provider, book_name=book_name, image=image, author=author, publishing_house=publishing_house, ISBN_number=ISBN_number, availability=availability, description=description)
        book.save()
        thank = True

    return render(request, 'dashboard.html', {'thank': thank})
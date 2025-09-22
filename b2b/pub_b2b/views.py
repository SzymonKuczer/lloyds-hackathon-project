from django.shortcuts import render


# Home page view
def homepage(request):
    return render(request, '../templates/homepage.html')


# About page view
def about(request):
    return render(request, 'about.html')


# Login page view
def login(request):
    return render(request, 'login.html')


# Register page view
def register(request):
    return render(request, 'register.html')


# Optional: main index view
def pub_b2b(request):
    return render(request, 'homepage.html')

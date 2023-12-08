from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from .models import Product  # Import your Product model

def index(request):
    return render(request, 'index.html')

def homepage(request):
    new_user = request.session.pop('new_user', None)  
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'HomePage.html', {'new_user': new_user, 'products': products})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            request.session['new_user'] = username
            return redirect('HomePage')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

class MyLoginView(LoginView):
    template_name = 'login.html'

from .models import Product, Category  # Import your Category model

def homepage(request):
    new_user = request.session.pop('new_user', None)
    products = Product.objects.all()
    categories = Category.objects.all()  # Retrieve all categories from the database
    return render(request, 'HomePage.html', {
        'new_user': new_user,
        'products': products,
        'categories': categories
    })

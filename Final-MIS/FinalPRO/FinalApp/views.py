from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from .models import Product, Category
from django.shortcuts import get_object_or_404, render



def index(request):
    return render(request, 'index.html')


def homepage(request):
    new_user = request.session.pop('new_user', None)
    products = Product.objects.all()
    categories = Category.objects.all() 
    return render(request, 'HomePage.html', {
        'new_user': new_user,
        'products': products,
        'categories': categories
    })


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



def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})



from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_page(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'category_page.html', {'category': category, 'products': products})



# WE ARE SEARHCING IN CATEGORY PAGE FOR A PRODUST USING THE BEWLO VIEW FUNC


def search_products(request, category_name):
    search_query = request.GET.get('search_query', '')
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category, name__icontains=search_query)
    
    return render(request, 'category_page.html', {'category': category, 'products': products})




from django.shortcuts import render

def homepage_view(request):
    return render(request, 'Homepage.html')

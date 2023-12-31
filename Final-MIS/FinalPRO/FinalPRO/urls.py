"""
URL configuration for FinalPRO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FinalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Homepage/', views.homepage, name='HomePage'),
    path('register/', views.register, name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('Homepage/<str:category_name>/', views.category_page, name='category_page'),
    path('Homepage/<str:category_name>/search/', views.search_products, name='product_search'),




]


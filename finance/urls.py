"""
URL configuration for finance project.

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
from .views import home, earnings_list, expenses_list,delete_expenses,delete_services,edit_expenses, add_earnings,delete_earning, edit_earning, add_expenses, login_view, services
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('earnings/', earnings_list, name='earnings_list'),
    path('expenses/', expenses_list, name='expenses_list'),
    path('add_earnings/', add_earnings, name='add_earnings'),
    path('add_expenses/', add_expenses, name='add_expenses'),
    path('services/', services, name='services'),
     path('earnings/delete/<int:earning_id>/', delete_earning, name='delete_earning'),
     path('earnings/edit/<int:earning_id>/', edit_earning, name='edit_earning'),
     path('expenses/delete/<int:expenses_id>/', delete_expenses, name='delete_expenses'),
     path('expenses/edit/<int:expenses_id>/', edit_expenses, name='edit_expenses'),
     path('services/delete/<int:services_id>/', delete_services, name='delete_services'),

]

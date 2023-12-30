from django.shortcuts import render, redirect, get_object_or_404
from .models import Earnings, Expenses, Service
from django.db.models import Sum
from .forms import EarningsForm, ExpensesForm, ServiceForm
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm 
from datetime import datetime, timedelta

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your home page
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    # Get the current month
    current_month = datetime.now().month

    # Calculate total earnings for the month
    total_earnings_month = Earnings.objects.filter(date__month=current_month).aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate total expenses for the month
    total_expenses_month = Expenses.objects.filter(date__month=current_month).aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate total all-time earnings
    total_all_time_earnings = Earnings.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate total all-time expenses
    total_all_time_expenses = Expenses.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate total revenue
    total_revenue = total_all_time_earnings - total_all_time_expenses

    # yearly revenue from expenses

    yearly_revenue= Service.objects.aggregate(Sum('amount_due'))['amount_due__sum'] or 0
    context = {
        'total_earnings_month': total_earnings_month,
        'total_expenses_month': total_expenses_month,
        'total_revenue': total_revenue,
        'yearly_revenue': yearly_revenue,
    }

    return render(request, 'home.html', context)

def earnings_list(request):
    earnings = Earnings.objects.all()
    return render(request, 'earnings_list.html', {'earnings': earnings})
def delete_earning(request, earning_id):
    earning = get_object_or_404(Earnings, id=earning_id)
    
    if request.method == 'POST':
        # Handle the deletion
        earning.delete()
        return redirect('earnings_list')  # Redirect to the earnings list page

    return render(request, 'delete_earning_confirm.html', {'earning': earning})

def edit_earning(request, earning_id):
    earning = get_object_or_404(Earnings, id=earning_id)

    if request.method == 'POST':
        form = EarningsForm(request.POST, instance=earning)
        if form.is_valid():
            form.save()
            return redirect('earnings_list')
    else:
        form = EarningsForm(instance=earning)

    return render(request, 'edit_earning.html', {'form': form, 'earning': earning})
def add_earnings(request):
    if request.method == 'POST':
        form = EarningsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('earnings_list')
    else:
        form = EarningsForm()
    return render(request, 'add_earnings.html', {'form': form})
def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', {'expenses': expenses})


def delete_expenses(request, expenses_id):
    expenses = get_object_or_404(Expenses, id=expenses_id)
    
    if request.method == 'POST':
        # Handle the deletion
        expenses.delete()
        return redirect('expenses_list')  # Redirect to the earnings list page

    return render(request, 'delete_expenses_confirm.html', {'expenses': expenses})

def edit_expenses(request, expenses_id):
    expenses = get_object_or_404(Expenses, id=expenses_id)

    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    else:
        form = ExpensesForm(instance=expenses)

    return render(request, 'edit_expenses.html', {'form': form, 'expenses': expenses})
def add_expenses(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')
    else:
        form = ExpensesForm()
    return render(request, 'add_expenses.html', {'form': form})

def services(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            # Process the form data
            service = form.save(commit=False)

            # Calculate and set the due date based on the current date and months_valid
            service.due_date = datetime.now().date() + timedelta(days=(form.cleaned_data['months_valid'] * 30))

            # Set a default value for amount_due (adjust as needed)
            # service.amount_due = 100.0  # For example, setting it to a default value of 100.0

            # Save the service to the database
            service.save()

            return redirect('services')  # Redirect to the services page after form submission
    else:
        form = ServiceForm()

    # Retrieve booked services
    booked_services = Service.objects.all()

    return render(request, 'services.html', {'form': form, 'booked_services': booked_services})
def delete_services(request, services_id):
    services = get_object_or_404(Service, id=services_id)
    
    if request.method == 'POST':
        # Handle the deletion
        services.delete()
        return redirect('services')  # Redirect to the earnings list page

    return render(request, 'delete_expenses_confirm.html', {'services': services})
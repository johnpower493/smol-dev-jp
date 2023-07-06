from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html')

def contact(request):
    return render(request, 'portfolio_app/contact.html')

def portfolio(request):
    return render(request, 'portfolio_app/portfolio.html')
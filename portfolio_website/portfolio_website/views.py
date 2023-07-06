```python
from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_website/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_website/about.html')

def contact(request):
    return render(request, 'portfolio_website/contact.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_website/portfolio.html', {'projects': projects})
```
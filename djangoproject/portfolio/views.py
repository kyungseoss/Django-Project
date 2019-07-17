from django.shortcuts import render
from .models import portfolio
# Create your views here.

def portfolio(request):
    portfolios = portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios' : portfolios})

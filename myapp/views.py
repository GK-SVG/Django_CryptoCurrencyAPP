from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def Home(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    context = {'data': data}
    return render(request, 'home.html', context)

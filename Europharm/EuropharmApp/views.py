from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'EuropharmApp/index.html')
def about(request):
    return render(request, 'EuropharmApp/about.html')
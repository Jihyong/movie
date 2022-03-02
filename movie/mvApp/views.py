from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    print('>>>> index')
    return render(request, 'mvApp/index.html')
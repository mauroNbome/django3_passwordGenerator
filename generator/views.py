from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz') # thats the way to grab information from html request

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('+!@#$%&')    
    if request.GET.get('numbers'):
        characters.extend('0123456789') 
    length = int(request.GET.get('length')) # remember to turn into int, all request stuff are string by default

    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
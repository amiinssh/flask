from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZX'))
    if request.GET.get('digits'):
        char.extend(list('1234567890')) 
    if request.GET.get('symbols'):
        char.extend(list('~!@#$%^&*()_+?><|\/,.')) 
        
    length = int(request.GET.get('length', 10))    
              
    password = ""
    for x in range(length):
        password +=random.choice(char)
    return render(request, 'password.html', {'password': password})
from django.shortcuts import render
from django.http import HttpResponse

def simple(request):
    return render(request, 'simple.html')
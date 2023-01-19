from django.shortcuts import render

def rest(request):
    return render(request, 'index.html')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
arr = ['alo paratta', 'potato']
def product(request):
    for i in range(0,len(arr)):
        if i == 0:
            # value = print(arr[i])
            return HttpResponse("Lunch is Alo Paratta")
        # return HttpResponse(i)
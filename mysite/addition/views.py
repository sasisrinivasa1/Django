from django.shortcuts import render

def plus(request):
    return render(request, 'numbers.html')
def add(request):
    num1 = request.POST['n1']
    num2 = request.POST['n2']
    result = int(num1) + int(num2)
    return render(request, 'result.html', {'result':result})

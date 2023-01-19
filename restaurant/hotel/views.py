from django.shortcuts import render,redirect
from hotel.models import RestHotel
from django.contrib.auth.models import User
from django.contrib import auth, messages
def hotel(request):
    items1 = RestHotel.objects.get(name = 'Curd Rice')
    items2 = RestHotel.objects.get(name = 'Chicken Biriyani')
    items3 = RestHotel.objects.get(name = 'Pepper Chicken')
    # items1.name = 'Grill Chicken'
    # items1.desc = 'Its an famous and tasty Indian food.'
    # items1.price = 5
    # items1.image = 'tandoori.png'
    # items2.name = 'Chicken Biriyani'
    # items2.desc = 'Spicy and Hyderbadi style Biriyani with Chicken Leg pieces.'
    # items2.price = 7
    # items2.image = 'chicken-biriyani.png'
    # items3.name = 'Mutton Biriyani'
    # items3.desc = 'Meat Mutton Biriyani with delicious smell and taste.'
    # items3.price = 9
    # items3.image = 'mutton-biriyani.png'
    return render(request, 'index.html',{'item1':items1,'item2': items2,'item3':items3})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        email = request.POST['EmailID']
        username = request.POST['Username']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,'email already taken') 
                return redirect('register')               
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                redirect ('login')
        return redirect('/restaurant/hotel/accounts/login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect ('/restaurant/hotel')
        else:
            messages.info(request,'Username Not found')
            return redirect ('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/restaurant/hotel')
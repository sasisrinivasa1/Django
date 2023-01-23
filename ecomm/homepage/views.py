from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from homepage.utils import generate_token, TokenGenerator
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        print(username)
        if password == confirm_password:
            print("Hello")
            if User.objects.filter(username=username).exists():
                print("Username Already Taken")
                messages.info(request,'Username Already Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                print("Email Already Taken")
                messages.info(request,'Email Already Taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                email_subject = "Activate your Account"
                email_message = render_to_string('auth/activate.html,{
                    'user':user,'domain':'http://127.0.0.1:8000/',
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user)
                    })
                email = EmailMessage(email_subject,email_message,settings.EMAIL_HOST_USER,['ssasikumar9651@gmail.com'],)
                EmailThread(email).start()
                messages.info(request,'Signup succesful')
                return redirect('/ec/login')
        else:
            messages.info(request,'Please check the password')
            return redirect('/signup')
    else:
        return render(request,'auth/signup.html')

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,'Account activated successfully')
            return redirect('/ec/login')
        return render(request,'auth/activatefail.html')

def handlelogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)   
        if user is not None:
            auth.login(request, user)
            return redirect('/ec')
        else:
            messages.info(request,'Incorrect Username/Password')
            return redirect('/ec/login')
    else:
        return render(request,'auth/login.html')

def handlelogout(request):
    auth.logout(request)
    return redirect('/ec')


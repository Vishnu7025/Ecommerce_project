from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        return render (request,'login.html')

    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:           
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'register.html')


def logout(request):
     auth.logout(request)
     return redirect('/')


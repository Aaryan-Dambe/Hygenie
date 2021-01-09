from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= user_name, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')
def register(request):


    if request.method == 'POST':
        user_name = request.POST['username']
        full_name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email = email).exists():
                print("Email ID Taken")
                messages.info(request,"Email ID Taken")


            elif User.objects.filter(username = user_name).exists():
                print('User Name is already Taken')
                messages.info(request,'User Name is already Taken')

            else:
                user = User.objects.create_user(username=user_name,
                                                first_name=full_name,
                                                email=email,
                                                password=password1)
                user.save()
                print("User Has Been Created !")
                return redirect('/')

        else:
            print("Password Don`t Match")
            messages.info(request , "Password Don`t Match")



    return render(request, 'register.html')

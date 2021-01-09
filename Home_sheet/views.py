from django.shortcuts import render
import random
x = ['Tony', 'Anisha' , 'Aaryan','AD9']


def index(request):



    return render(request, 'home_page.html', {'name' : random.choice(x) })

def addition(request):
    x = int(request.POST['num1'])
    y = int(request.POST['num2'])
    add = x + y
    return render(request, 'result.html',{'res': add})




# Create your views here.

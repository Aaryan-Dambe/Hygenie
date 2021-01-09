from django.shortcuts import render
from . models import profit
# Create your views here.
def search(request):
    val = request.GET['query']
    all_post = profit.objects.filter(name__icontains= val)
    data = {'pro' : all_post}
    return render(request, 'Search_Result.html', data)

def index(request):
    return render(request, 'index.html', {'price' : 1000})

def courses(request):
    multi_profit = profit.objects.all()
    return render(request,'courses.html' , {'products': multi_profit} )

def about(request):
    return render(request, 'about.html')





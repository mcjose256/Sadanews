from django.shortcuts import render


def home(request):
    return render(request,'base/home.html')

def room(request):
    return render(request,"room.html")


# Create your views here.

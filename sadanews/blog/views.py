from django.shortcuts import render


def post_list(request):
    return render(request,'blog/postlist.html')
    
#def room(request):
    #return render(request,"room.html")


# Create your views here.

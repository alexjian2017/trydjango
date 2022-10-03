from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)      # <WSGIRequest: GET '/'>
    print(args, kwargs) # () {}
    #return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'home.html',{})

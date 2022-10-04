from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request)      # <WSGIRequest: GET '/'>
    #print(args, kwargs) # () {}
    print(request.user)
    my_context = {
        'name':'程序元阿源',
        'age':27,
        'my_list':[123,456,789]
    }
    #return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'home.html',my_context)

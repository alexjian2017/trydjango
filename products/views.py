from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

def products_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object' : obj
    }
    return render(request, 'product/detail.html', context)

def products_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, 'product/create.html', context)

# def products_create_view(request):
#     #print(request.GET)
#     #print(request.POST)
#     my_new_title =request.POST.get('title')
#     print(my_new_title)
#     context = {}
#     return render(request, 'product/create.html', context)

# def products_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#     context = {
#         'form': my_form
#     }
#     return render(request, 'product/create.html', context)

def dynamic_lookup_view(request, my_id):
    #obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object' : obj,
    }
    return render(request, 'product/detail.html', context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'object' : obj,
    }
    return render(request, 'product/delete.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset,
    }
    return render(request, 'product/list.html', context)
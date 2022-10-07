
from django.urls import path
from .views import products_detail_view, products_create_view, dynamic_lookup_view,\
                            product_delete_view, product_list_view

app_name = 'products'
urlpatterns = [
    #path('product/', products_detail_view),
    path('', product_list_view,name='product-list'),
    path('create/', products_create_view,name='product-create'),
    path('<int:my_id>/',dynamic_lookup_view,name='product-detail'),
    path('<int:my_id>/delete',product_delete_view,name='product-delete'),
]
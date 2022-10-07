
from django.urls import path
#from .views import article_detail_view,article_list_view
from .views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView


app_name = 'blogs'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),

    #path('', article_list_view, name='article-list'),
    #path('<int:my_id>', article_detail_view, name='article-detail'),
]
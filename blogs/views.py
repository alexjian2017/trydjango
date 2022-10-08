from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.views import View

class CourseView(View):
    template_name = 'blogs/course_detail.html'
    def get(self,request, id = None, *args, **kwargs):
        context={}
        if id is not None:
            id_ = self.kwargs.get('id')
            obj = get_object_or_404(Article, id = id_)
            context['object'] = obj
        return render(request, self.template_name, context)

class ArticleListView(ListView):
    template_name = 'blogs/list.html'
    queryset = Article.objects.all()   #default會去找<App>/<model_name>_list.html

class ArticleCreateView(CreateView):
    template_name = 'blogs/create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'blogs/detail.html'
    #queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

class ArticleUpdateView(UpdateView):
    template_name = 'blogs/create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)
    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'blogs/delete.html'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)
    def get_success_url(self):
        return reverse('blogs:article-list')




# def article_detail_view(request, my_id):
#     obj = get_object_or_404(Article, id=my_id)
#     context = {
#         'object' : obj,
#     }
#     return render(request, 'blogs/detail.html', context)

# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         'object_list' : queryset,
#     }
#     return render(request, 'blogs/list.html', context)

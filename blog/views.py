from typing import Any
from django.views.generic import ListView, DetailView
from account.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from account.mixins import AuthorAccessMixin
from .models import Article, Category
# Create your views here.
# def index(request, page=1):
#     contact_list = Article.objects.published()
#     paginator = Paginator(contact_list, 1)
#     articles = paginator.get_page(page)
#     context = {
#         "articles" : articles,
        
#     }
#     return render(request, "index.html", context)
class ArticleView(ListView):
    queryset = Article.objects.published()
    paginate_by = 2
# def detail(request, slug):
#     context = {
#         "article" : get_object_or_404(Article.objects.published(), slug = slug)
#     }
#     return render(request, "detail.html", context)
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
    
class ArticlePreview(AuthorAccessMixin, DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

# def category(request, slug, page=1):
#     category = get_object_or_404(Category,slug = slug ,status=True)
#     contact_list = category.articles.published()
#     paginator = Paginator(contact_list, 2)
#     articles = paginator.get_page(page)
#     context = {
#         'category' : category,
#         'articles' : articles
#     }
#     return render(request,'category.html',context)

class CategoryList(ListView):
    paginate_by = 2
    template_name = 'blog/category_list.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug = slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by = 2
    template_name = 'blog/author_list.html'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username = username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
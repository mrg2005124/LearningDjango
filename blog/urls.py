from django.urls import path
from .views import  ArticleView, ArticleDetail, CategoryList, AuthorList

app_name = 'blog'

urlpatterns = [
    path('', ArticleView.as_view(), name = 'index'),
    path('page/<int:page>', ArticleView.as_view(), name = 'index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name = 'detail'),
    path('category/<slug:slug>',CategoryList.as_view(), name = 'category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name = 'category'),
     path('author/<slug:username>',AuthorList.as_view(), name = 'author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name = 'author')
]

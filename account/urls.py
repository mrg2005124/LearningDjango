from django.contrib.auth import views
from django.urls import path
from .views import ArticleList, ArticleCreate, ArticleUpdate
app_name = 'account'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
]

urlpatterns += [
    path('', ArticleList.as_view(), name = 'home'),
    path('article/create', ArticleCreate.as_view(), name = 'article_create'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name = 'article_update'),
]

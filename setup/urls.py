from django.contrib import admin
from django.urls import path, include, re_path
from account.views import Login, Register, activate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('login/', Login.as_view, name='login'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('register/', Register.as_view(), name='register'),
path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #show media (debug mode)
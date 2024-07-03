from django.contrib import admin
from .models import Article,Category,IpAddress
# Register your models here.

admin.site.site_header = 'وبلاگ جنگویی من'

def make_published(modeladmin, request, queryset):
    query = queryset.update(status = 'p')
    if query == 1:
        message = 'منتشر شد'
    else:
        message = 'منتشر شدند'
    modeladmin.message_user(request,f'{query} مقاله {message}')
make_published.short_description = 'منتشر کردن'

def make_draft(modeladmin, request, queryset):
    query = queryset.update(status = 'd')
    if query == 1:
        message = 'پیش نویس شد'
    else:
        message = 'پیش نویس شدند'
    modeladmin.message_user(request, f'{query} مقاله {message}')
make_draft.short_description = 'پیش نویس کردن'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug', 'parent','status')
    list_filter = (['status'])
    search_filter = ('title','slug')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['position']
admin.site.register(Category, CategoryAdmin)

# Admin panel table setting
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'author','is_special','jpublished', 'status', 'str_category')  #titles
    list_filter = ('title', 'published', 'status')  #filters
    search_filter = ('title','description')  #search in: 
    prepopulated_fields = {'slug' : ('title',)}  #auto complete  field {myfield:(source)}
    ordering = ['-status','published']
    actions = [make_published,make_draft]


admin.site.register(Article, ArticleAdmin)  #send to admin panel (model name,table setting name)
admin.site.register(IpAddress)  #send to admin panel (model name,table setting name)
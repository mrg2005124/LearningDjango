from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
from django.utils.html import format_html
from extension.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status ='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status =True)

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته بندی')
    title = models.CharField(max_length=200, verbose_name='دسته بندی عنوان')
    slug = models.SlugField(max_length=100, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default= True, verbose_name='آیا نمایش داده شود؟ ')
    position = models.IntegerField(verbose_name='پوزیشن')
    
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position']
    
    def __str__(self):
        return self.title
    objects = CategoryManager()
    
#  create database

class IpAddress(models.Model):
    ip = models.GenericIPAddressField(verbose_name='آدرس ایپی')
class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منشتر شده'),
        ('i','در حال بررسی'),
        ('b','عدم تایید')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name = 'articles', verbose_name = "نویسنده")
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, verbose_name='ادرس')
    category = models.ManyToManyField(Category,verbose_name='دسته بندی', related_name ='articles')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to="image", verbose_name='تصویر')  # upload to : saved and upload location image
    published = models.DateTimeField(default=timezone.now, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default= True, verbose_name='مقاله ویژه')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    comments = GenericRelation(Comment)
    hit = models.ManyToManyField(IpAddress, through='ArticleHit',blank=True,verbose_name='بازدید')

    # for persian admin panel
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['-published']
    
    # show title in django panel
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('account:home')

    def jpublished(self):
        return jalali_converter(self.published)
    jpublished.short_description = 'زمان انتشار'

    def category_published(self):
        return self.category.filter(status = True)
    def thumbnail_tag(self):
        return format_html(f"<img width=100 style='border-radius:5px;' src='{self.thumbnail.url}'>")
    thumbnail_tag.short_description = 'تصویر'

    def str_category(self):
        return ", ".join([category.title for category in self.category_published()])
    str_category.short_description = 'دسته بندی'
    objects = ArticleManager()

class ArticleHit(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE)
    ip = models.ForeignKey(IpAddress,on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
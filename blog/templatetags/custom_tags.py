from django import template
from ..models import Category ,Article
from django.db.models import Count,Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ اموزشی جنگو"

@register.inclusion_tag("blog/partials/category_nav.html")
def category_nav():
    return {
        "category" : Category.objects.filter(status = True)
    }

@register.inclusion_tag("blog/partials/top_articles.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days =30)
    return {
        'articles' : Article.objects.published().annotate(\
            count=Count('hit',filter = \
                Q(articlehit__created__gt=last_month)))\
                .order_by('-count','-published'),
                'title' : 'مقالات پر بازدید ماه'
    }

@register.inclusion_tag("blog/partials/top_articles.html")
def hot_articles():
    last_month = datetime.today() - timedelta(days =30)
    content_type = ContentType.objects.get(app_label="blog", model="article")
    return {
        'articles' : Article.objects.published().annotate(\
            count=Count('comments',filter = \
                Q(comments__posted__gt=last_month) \
                and \
                Q(comments__content_type_id=content_type)))\
                .order_by('-count','-published'),
                'title' : 'مقالات داغ ماه'
    }

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request" : request,
        "link_name" : link_name,
        "link" : f"account:{link_name}",
        "content" : content,
        "classes" : classes
    }
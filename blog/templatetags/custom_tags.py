from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ اموزشی جنگو"

@register.inclusion_tag("blog/partials/category_nav.html")
def category_nav():
    return {
        "category" : Category.objects.filter(status = True)
    }
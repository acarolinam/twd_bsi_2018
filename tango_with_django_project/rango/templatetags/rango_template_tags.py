from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.order_by('-views'),
            'act_cat': cat}
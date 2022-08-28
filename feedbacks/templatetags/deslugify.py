from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def deslugify(value: str):
    return value.replace('_', ' ')

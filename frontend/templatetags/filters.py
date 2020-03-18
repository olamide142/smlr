# Filter
from django import template

register = template.Library()

@register.filter(name='reduceLen')
def reduceLen(value, arg):
    if len(value) > arg:
        value = value[0:arg]
    return value

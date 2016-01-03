from django import template
from django.db import models
register = template.Library()

@register.filter
def attrvalue(var,arg):
    value = getattr(var,arg,'')
    if isinstance(value,models.Manager):
        return value.all()
    return value



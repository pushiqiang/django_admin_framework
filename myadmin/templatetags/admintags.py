from django.contrib.contenttypes.models import ContentType
from django import template
from django.db import models
register = template.Library()

@register.filter
def attrvalue(var,arg):
    value = getattr(var,arg,'')
    if isinstance(value,models.Manager):
        return value.all()
    return value
@register.inclusion_tag("myadmin/sidebar.html")
def content_admin():
    """ context processor for the site templates """
    labels = ContentType.objects.values("app_label").distinct().order_by('app_label')
    label_apps = []
    for label in labels:
        if label['app_label'] =='sessions':
            continue
	app_list = []
        label_app = {}
        label_name = label['app_label']
        apps = ContentType.objects.filter(app_label=label_name)
        app_count = apps.count()
        for app in apps:
            app_name_model = {}
            app_name_model['name'] = app.name
            app_name_model['model'] = app.model
            app_list.append(app_name_model)
            del app_name_model
        label_app['label_name'] = label_name
        label_app['app_count'] = app_count
        label_app['app_list'] = app_list
        label_apps.append(label_app)
        del app_list
        del label_app
        del apps

    return {
            'label_apps': label_apps
            #'request': request
            }



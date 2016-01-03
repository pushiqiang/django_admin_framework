#coding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'myadmin.views.Login',{'template_name':'myadmin/login.html'}, name='admin_login'),
    url(r'^logout/$', 'myadmin.views.Logout', name='admin_logout'),
    url(r'^$', 'myadmin.views.AdminIndex',{'template_name':'myadmin/admin_index.html'}, name='admin_index'),
    url(r'^(?P<label>\w+)/$', 'myadmin.views.LabelAppList', {'template_name':'myadmin/app_list.html'},name='label_list'), 
    url(r'^(?P<label>\w+)/(?P<name>\w+)/$', 'myadmin.views.ObjectList', 
		{'template_name':'myadmin/object_list.html'}, name='label_name_list'),   
    url(r'^(?P<label>\w+)/(?P<name>\w+)/add/$', 'myadmin.views.ObjectCreate',
		{'template_name':'myadmin/create_form.html'},name='object_add'), 
    url(r'^(?P<label>\w+)/(?P<name>\w+)/(?P<pk>\d+)/$', 'myadmin.views.ObjectUpdate',
		{'template_name':'myadmin/myadmin_form.html'}, name='object_update'),   	
    url(r'^(?P<label>\w+)/(?P<name>\w+)/(?P<pk>\d+)/delete/$', 'myadmin.views.ObjectDelete',
		{'template_name':'myadmin/delete_confirm.html'}, name='object_delete'),   	
)

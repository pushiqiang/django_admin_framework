# django_admin_framework
基于通用试图的admin框架<br>
新手入门之作，大神勿喷。<br>
为了方便采用了display views和editing views试图实现，使用到了自定义标签，context_process等<br>
添加数据页面由于了使用通用试图的form模式，很不美观，下一步准备去掉通用试图，加入搜索过滤功能。<br>
权限和认证系统还在学习中<br>
This is a django admin framework based on general views powerd by pushiqiang of rookie

邮箱：pushiqiang@126.com<br>
qq:983003089<br>
预览
=====
![github1](demo_img/g1.jpg)
![github2](demo_img/g2.jpg)
![github3](demo_img/g3.jpg)
![github4](demo_img/g4.jpg)
![github5](demo_img/g5.jpg)

运行使用
=====
1.设置settings
---
TEMPLATE_CONTEXT_PROCESSORS = (<br>
 　　　'myadmin.utils.context_processors.content_admin',<br>
)<br>
INSTALLED_APPS = (<br>
　　　　'myadmin',<br>
)
2.设置url
---
　　　　url(r'^myadmin/',include('myadmin.urls')),
3.设置admin_settings（可以不用设置）
---
　　　　在myadmin/admin_settings.py文件中设置要显示的field，默认显示所有的field,如xxx_admin = {'list_display':['name','description','status'],}，暂时只设置了list_display。





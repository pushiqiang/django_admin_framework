# django_admin_framework
基于通用试图的admin框架<br>
新手入门之作，大神勿喷。<br>
为了方便采用了display views和editing views试图实现，使用到了自定义标签，context_process等<br>
添加数据页面由于了使用通用试图的form模式，很不美观，下一步准备去掉通用试图，加入搜索过滤功能。<br>
This is a django admin framework base on class_based views powerd by pushiqiang of rookie

邮箱：pushiqiang@126.com<br>
qq:983003089<br>
预览
=====

运行使用
=====
![github1](4.pushiqiang.sinaapp.com/static/github_img/g1.jpg)
![github2](4.pushiqiang.sinaapp.com/static/github_img/g2.jpg)
![github3](4.pushiqiang.sinaapp.com/static/github_img/g3.jpg)
![github4](4.pushiqiang.sinaapp.com/static/github_img/g4.jpg)
![github5](4.pushiqiang.sinaapp.com/static/github_img/g5.jpg)
1.配置settings
---
TEMPLATE_CONTEXT_PROCESSORS = (<br>
          'myadmin.utils.context_processors.content_admin',<br>
)<br>
INSTALLED_APPS = (<br>
          'myadmin',<br>
)
2.配置url
---
url(r'^myadmin/',include('myadmin.urls')),

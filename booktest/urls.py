from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name="index"),   # rul 的参数name用于方向解析（在视图中重定向需要用到，用于二：模板中的链接）
    url(r"^(\d+)$", views.detail, name="detail"),
    # url(r"^(\d+)/(\d+)/(\d+)$", views.show, name="show"),
    url(r"^(?P<P1>\d+)/(?P<P2>\d+)/(?P<P3>\d+)$", views.show_kwargs, name="show_kwargs"),
    url(r"^getTest1/$", views.getTest1, name="getTest1"),
    url(r"^getTest2/$", views.getTest2, name="getTest2"),
    url(r"^getTest3/$", views.getTest3, name="getTest3"),
    url(r"^postTest1/$", views.postTest1, name="postTest1"),
    url(r"^postTest2/$", views.postTest2, name="postTest2"),
    url(r"^cookieTest1$", views.cookieTest1, name="cookieTest1"),
    url(r"^rederect$", views.rederect),
    url(r"^target_page$", views.target_page),

]
# url 包括 正则表达式路径  和 视图名（在视图里面的render函数中的templates参数定义了使用的哦模板） 和 name

"""
url讲解：

在正则表达式中加入小括号 获取匹配后的内容， 并且将它作为 对应视图函数的的一个参数

url(r'^(\d+)$', views, detail, name="detail")

"""

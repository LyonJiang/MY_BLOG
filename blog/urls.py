# coding:utf8
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^post/(?P<id>\d+)/$',views.Detail,name="blog_detail"),
    url(r'^home/',views.home,name="blog_home"),
    # url(r'',views.home,name="home"),
    url(r'^test/', views.Test, name="blog_test"),

    url(r'^login/', views.login, name="blog_login"),
    url(r'^register/', views.register, name="blog_register"),


]
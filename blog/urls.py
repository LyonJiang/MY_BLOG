# coding:utf8
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^post/(?P<id>\d+)/$',views.Detail,name="blog_detail"),
    url(r'^home/',views.home,name="blog_home"),
    # url(r'',views.home,name="home"),

    url(r'^login/', views.login, name="blog_login"),
    url(r'^logout/', views.logout, name="blog_logout"),
    url(r'^register/', views.register, name="blog_register"),
    url(r'^index/', views.index, name="blog_index"),
    url(r'^singlepost/', views.single, name="blog_single"),


]
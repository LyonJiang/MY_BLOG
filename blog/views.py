# coding:utf8
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article
from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request,'blog/index.html')
def single(request):
    return render(request,'blog/singlepost.html')

def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html',{'post':post})
# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list': post_list})


def register(request):
    error=[]
    username=None
    password=None
    password2=None
    email = None
    CompareFlag=False
    if request.method=="POST":
        if not request.POST.get('username'):
            error.append("请输入用户名")
        else:
            username=request.POST.get('username')
        if not request.POST.get('password'):
            error.append('请输入密码')
        else:
            password=request.POST.get('password')
        if not request.POST.get('password2'):
            error.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')

        if not request.POST.get('email'):
            error.append('请输入邮箱')
        else:
            email=request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                error.append('两次输入密码不一致')

        if username is not None and password is not None and email is not None  and CompareFlag:
            user=User.objects.create_user(username,email,password)
            user.save()
            return render(request, 'blog/register2.html', {'error': error})

    return render(request,'blog/register.html',{'error':error})



def login(request):
    errors = []
    username = None
    password = None
    if request.method == "POST":
        if not request.POST.get('username'):
            errors.append('用户名不能为空')
        else:
            username = request.POST.get('username')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return render(request, 'blog/login2.html', {'errors': errors})
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')
    return render(request, 'blog/login.html', {'errors': errors})


def logout(request):
    auth.logout(request)
    return render(request,'blog/base.html')
import hashlib
import random
import time
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User


def index(request):
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'username':user.username})
    else:
        return render(request, 'index.html')

# 生成token
def generate_token():
    token = str(time.time()) + str(random.random)
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()

# 加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        # 存数据库
        try:
            user = User()
            user.username = username
            # 密码加密
            user.password = generate_password(password)
            user.tel = tel
            user.token = uuid.uuid5(uuid.uuid4(), 'register')
            user.save()

            response = redirect('app:index')
            # 状态保持
            response.set_cookie('token', user.token)
            return response
        except Exception as e:
            return HttpResponse('注册失败')



# 登录
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        # 验证
        password = generate_password(request.POST.get('password'))

        users = User.objects.filter(username=username, password=password)
        if users.exists():
            user = users.first()
            user.token = generate_token()
            user.save()
            response = redirect('app:index')
            response.set_cookie('token', user.token)
            return response
        else:
            return HttpResponse('用户名或密码错误')


def loginout(request):
    response = redirect('app:index')

    response.delete_cookie('token')
    return response
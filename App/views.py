import hashlib
import random
import time
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User, SildePic

# 主页
def index(request):
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)


    # img_src1 = SildePic.objects.filter(id=1)
    # img_src1 ='/static/' + img_src1.first().img_src
    #
    # img_src2 = SildePic.objects.filter(id=2)
    # img_src2 = '/static/' + img_src2.first().img_src
    # img_src3 = SildePic.objects.filter(id=3)
    # img_src3 = '/static/' + img_src3.first().img_src
    # img_src4 = SildePic.objects.filter(id=4)
    # img_src4 = '/static/' + img_src4.first().img_src
    # img_src5 = SildePic.objects.filter(id=5)
    # img_src5 = '/static/' + img_src5.first().img_src
    # img_src6 = SildePic.objects.filter(id=6)
    # img_src6 = '/static/' + img_src6.first().img_src
    # img_src7 = SildePic.objects.filter(id=7)
    # img_src8 = '/static/' + img_src7.first().img_src
    img_srcs = SildePic.objects.all()
    if users.exists():
        user = users.first()
        # return render(request, 'index.html', context={'username':user.username,'img_src1':img_src1,'img_src2':img_src2,'img_src3':img_src3,'img_src4':img_src4,'img_src5':img_src5,'img_src6':img_src6,'img_src7':img_src7})
        return render(request, 'index.html', context={'username':user.username,'img_srcs':img_srcs})

    else:
        # return render(request, 'index.html', context={'img_src1':img_src1,'img_src2':img_src2,'img_src3':img_src3,'img_src4':img_src4,'img_src5':img_src5,'img_src6':img_src6,'img_src7':img_src7})
        return render(request, 'index.html', context={'img_srcs':img_srcs})


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

# 退出登录
def loginout(request):
    response = redirect('app:index')

    response.delete_cookie('token')
    return response

# 详情页
def goodDetail(request):
    return None

# 购物车
def goodShopCart(request):
    return None


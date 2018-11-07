import hashlib
import random
import time
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User, SildePic, SmallSildePic


# 主页
def index(request):
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    img_srcs = SildePic.objects.all()
    smallsildepics = SmallSildePic.objects.all()
    if users.exists():
        user = users.first()
        data = {
            'account':user.account,
            'img_srcs':img_srcs,
            'smallsildepics': smallsildepics,

        }
        return render(request, 'index.html', context=data)

    else:
        return render(request, 'index.html', context={'img_srcs': img_srcs})


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
        account = request.POST.get('account')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        # 存数据库
        try:
            user = User()
            user.account = account
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
        account = request.POST.get('account')
        password = request.POST.get('password')
        # 验证
        try:
            user = User.objects.get(account=account)
            if user.password == generate_password(password):  # 登录成功

                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('app:index')
            else:  # 登录失败
                return render(request, 'login.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'login.html', context={'acountErr': '账号不存在!'})


# 账号验证
def checkaccount(request):
    account = request.GET.get('account')
    print(account)
    responseData = {
        'msg': '账号可用',
        'status': 1  # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


# 手机号验证
def checktel(request):
    tel = request.GET.get('tel')
    print(tel)
    responseData = {
        'msg': '手机号可用',
        'status': 1  # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(tel=tel)
        responseData['msg'] = '手机账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


# 退出登录
def loginout(request):
    request.session.flush()
    return redirect('app:index')


# 详情页
def goodDetail(request):
    return None


# 购物车
def goodShopCart(request):
    return None


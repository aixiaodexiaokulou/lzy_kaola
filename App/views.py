import hashlib
import random
import time
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User, SildePic, SmallSildePic, Goods, Cart, Order, OrderGoods


# 主页
def index(request):
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    img_srcs = SildePic.objects.all()
    smallsildepics1 = SmallSildePic.objects.all()[0:4]
    smallsildepics2 = SmallSildePic.objects.all()[4:8]
    smallsildepics3 = SmallSildePic.objects.all()[8:12]

    if users.exists():
        user = users.first()
        data = {
            'account': user.account,
            'img_srcs': img_srcs,
            'smallsildepics1': smallsildepics1,
            'smallsildepics2': smallsildepics2,
            'smallsildepics3': smallsildepics3,

        }
        return render(request, 'index.html', context=data)

    else:
        return render(request, 'index.html', context={'img_srcs': img_srcs, 'smallsildepics1': smallsildepics1,
                                                      'smallsildepics2': smallsildepics2,
                                                      'smallsildepics3': smallsildepics3, })


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
    # print(tel)
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


#
def loginoutdetail(request):
    request.session.flush()
    return redirect('app:index')


def loginoutcart(request):
    request.session.flush()
    return redirect('app:index')


# 商品详情页
def goods(request, id):
    # goods = Goods.objects.all()[0:1]
    # 根据ID获取对应商品数据
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    goodsList = Goods.objects.filter(id=id)

    if users.exists():
        user = users.first()
        # 获取购物车角标
        carts = Cart.objects.filter(user=user)
        count = 0
        for cart in carts:
            count += cart.number
        data = {
            'account': user.account,
            'goodsList': goodsList,
            'carts': carts,
            'count': count,
        }
        return render(request, 'goodDetail.html', context=data)
    else:
        return render(request, 'goodDetail.html', context={'goodsList': goodsList})


# 购物车
def goodShopCart(request):
    token = request.session.get('token')
    users = User.objects.filter(token=token)

    if users.exists():
        user = users.first()
        carts = Cart.objects.filter(user=user).exclude(number=0)

        data = {
            'account': user.account,
            'carts': carts,
        }
        return render(request, 'goodShopCart.html', context=data)

    else:
        return redirect('app:login')


# 添加到购物车
def addcart(request):
    goodsid = request.GET.get('goodsid')
    # print(goodsid)
    goodsnum = request.GET.get('goodsnum')
    goodsnum1 = int(goodsnum)
    print(type(goodsnum1))
    token = request.session.get('token')

    responseDate = {
        'msg': '添加商品到购物车成功',
        'status': 1,

    }
    if token:
        user = User.objects.get(token=token)
        goods = Goods.objects.get(pk=goodsid)

        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number + goodsnum1
            cart.save()
            responseDate['number'] = cart.number

        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1
            cart.save()
            responseDate['number'] = cart.number

        return JsonResponse(responseDate)
    else:
        responseDate['msg'] = '未登录 请登陆后操作'
        responseDate['status'] = -1
        return JsonResponse(responseDate)


# 购物车内加
def cartadd(request):
    goodsid = request.GET.get('goodsid')
    # print(goodsid)
    token = request.session.get('token')
    responseData = {
        'msg': '商品数量加1',
        'status': 1,
    }
    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodsid)

    carts = Cart.objects.filter(user=user).filter(goods=goods)
    cart = carts.first()
    cart.number = cart.number + 1
    cart.save()
    responseData['number'] = cart.number

    return JsonResponse(responseData)


# 购物车内减
def cartsub(request):
    goodsid = request.GET.get('goodsid')
    # print(goodsid)
    token = request.session.get('token')
    responseData = {
        'msg': '商品数量减1',
        'status': 1,
    }
    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodsid)

    carts = Cart.objects.filter(user=user).filter(goods=goods)
    cart = carts.first()
    cart.number = cart.number - 1
    cart.save()
    responseData['number'] = cart.number

    return JsonResponse(responseData)


# 购物车删除
def dropgood(request):
    goodsid = request.GET.get('goodsid')
    # print(goodsid)
    token = request.session.get('token')
    responseData = {
        'msg': '删除一个商品',
        'status': -1,
    }
    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodsid)

    carts = Cart.objects.filter(user=user).filter(goods=goods)
    # cart = carts.first()
    carts.delete()
    responseData['msg'] = '删除成功'

    return JsonResponse(responseData)

# 购物车内单选中
def oneselect(request):
    cartid = request.GET.get('cartid')
    checked = request.GET.get('checked')
    # print(cartid)
    cart = Cart.objects.get(pk=cartid)
    # cart.isselect = not cart.isselect
    if checked == 'true':
        cart.isselect = True
    elif checked == 'false':
        cart.isselect = False

    cart.save()

    responseData = {
        'msg': '单选状态改变',
        'status': 1,
        'isselect': cart.isselect
    }

    return JsonResponse(responseData)

# 购物车内全选
def allselect(request):
    isselect = request.GET.get('isselect')

    if isselect == 'true':
        isselect = True
    else:
        isselect = False

    token = request.session.get('token')
    user = User.objects.get(token=token)
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        cart.isselect = isselect
        cart.save()

    return JsonResponse({'msg':'反选操作成功','status':1})

# 订单
def generateorder(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)

    # 生成订单
    order = Order()
    order.user = user
    order.identifier = str(int(time.time())) + str(random.randrange(10000,100000))
    order.save()

    # 订单商品
    carts = Cart.objects.filter(user=user).filter(isselect=True)
    for cart in carts:
        orderGoods = OrderGoods()
        orderGoods.order = order
        orderGoods.goods = cart.goods
        orderGoods.number = cart.number
        orderGoods.save()

        # 移除购物车商品
        cart.delete()

    responseData = {
        'msg':'订单生成成功',
        'status':1,
        'identifier': order.identifier
    }

    return JsonResponse(responseData)

# 订单详情
def orderinfo(request,identifier):
    # 一个订单可以有多个商品
    order = Order.objects.get(identifier=identifier)



    return render(request,'orderinfo.html',context={'order':order})
from django.db import models

# Create your models here.
# 注册登录 用户
class User(models.Model):
    account = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=20,unique=True)
    # 令牌: 唯一标识
    token = models.CharField(max_length=256, default='')

# 轮播图
class SildePic(models.Model):
    img_src = models.CharField(max_length=1000)

# 小轮播图
class SmallSildePic(models.Model):
    small_src = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    discount_price = models.CharField(max_length=100)
    orig_price = models.CharField(max_length=100)

# 商品
class Goods(models.Model):
    small_src = models.CharField(max_length=100 ,null=True)
    middle_src = models.CharField(max_length=100,null=True)
    big_src = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=256,null=True)
    des = models.CharField(max_length=256,null=True)
    active_name = models.CharField(max_length=100,null=True)
    active_content = models.CharField(max_length=100,null=True)
    discount_price = models.CharField(max_length=100,null=True)
    discount = models.CharField(max_length=100,null=True)
    orig_price = models.CharField(max_length=100,null=True)
    tax = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    self = models.BooleanField()
    cross1 = models.BooleanField()

# 购物车
class Cart(models.Model):
    # 用户(通过外键建立关系)
    user = models.ForeignKey(User)
    # 商品(通过外键建立关系)
    goods = models.ForeignKey(Goods)
    # 商品数量
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)

# 订单
class Order(models.Model):
    user = models.ForeignKey(User)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)

    # 订单状态
    # -1 过期
    # 1 未付款
    # 2 已付款,未发货
    # 3 已发货,快递
    # 4 已签收,未评价
    # 5 已评价
    # 6 退款....
    status = models.IntegerField(default=1)

    # 订单号
    identifier = models.CharField(max_length=256)

# 订单商品
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(Goods)
    # 个数
    number = models.IntegerField(default=1)


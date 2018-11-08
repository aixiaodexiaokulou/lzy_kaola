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
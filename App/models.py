from django.db import models

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=20,unique=True)
    # 令牌: 唯一标识
    token = models.CharField(max_length=256, default='')

# 轮播图
class SildePic(models.Model):
    img_src = models.CharField(max_length=1000)
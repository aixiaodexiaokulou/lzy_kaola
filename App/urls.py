from django.conf.urls import url

from App import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 注册
    url(r'^register/$', views.register, name='register'),
    # 登录
    url(r'^login/$', views.login, name='login'),
    # 退出登录
    url(r'^loginout/$', views.loginout, name='loginout'),

    # 详情页
    url(r'^goodDetail/$', views.goodDetail, name='goodDetail'),
    # 购物车
    url(r'^goodShopCart/$', views.goodShopCart, name='goodShopCart'),

]
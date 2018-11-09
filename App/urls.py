from django.conf.urls import url

from App import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 注册
    url(r'^register/$', views.register, name='register'),
    # 验证账号是否已被注册
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),
    # 验证手机是否已被注册
    url(r'^checktel/$', views.checktel, name='checktel'),

    # 登录
    url(r'^login/$', views.login, name='login'),
    # 退出登录
    url(r'^loginout/$', views.loginout, name='loginout'),
    # 退出详情页登录
    url(r'^loginoutdetail/$', views.loginoutdetail, name='loginoutdetail'),
    # 购物车页登录
    url(r'^loginoutcart/$', views.loginoutcart, name='loginoutcart'),

    # 详情页
    url(r'^goods/(\d+)/$', views.goods, name='goods'),
    # 购物车
    url(r'^goodShopCart/$', views.goodShopCart, name='goodShopCart'),

]

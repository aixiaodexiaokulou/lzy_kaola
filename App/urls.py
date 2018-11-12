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

    url(r'^addcart/$', views.addcart, name='addcart'),  # 添加到购物车表Ajax

    # 购物车
    url(r'^goodShopCart/$', views.goodShopCart, name='goodShopCart'),

    # 购物车内加
    url(r'^cartadd/$', views.cartadd, name='cartadd'),
    # 购物车内减
    url(r'^cartsub/$', views.cartsub, name='cartsub'),
    # 购物车内删除
    url(r'^dropgood/$', views.dropgood, name='dropgood'),
    # 购物车内单选中
    url(r'^oneselect/$', views.oneselect, name='oneselect'),
    # 购物车内全选
    url(r'^allselect/$', views.allselect, name='allselect'),

    # 下单
    url(r'^generateorder/$', views.generateorder, name='generateorder'),
    # 订单详情
    url(r'^orderinfo/(\d+)/$', views.orderinfo, name='orderinfo'),


]

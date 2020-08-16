from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^tea-list/$', views.ShopList.as_view())
    # url(r'^tea-list/$', views.ShopList.as_view(), name='tea') #teashop/tea-list/
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hoso/', views.hoso, name="hoso"),
    path('checkout/', views.checkout, name="checkout"),
    path('dangky/', views.dangky, name="dangky"),
    path('dangnhap/', views.dangnhap, name="dangnhap"),
    path('dangxuat/', views.dangxuat, name="dangxuat"),
    path('search/', views.search, name="search"),
    path('Top100/', views.Top100, name="Top100"),
    path('nghe/', views.nghe, name="nghe"),
    path('nghe1/', views.nghe1, name="nghe1"),
    path('khampha/', views.khampha, name="khampha"),
    path('baihat/', views.baihat, name='baihat'),
    path('album/', views.album, name='album'),
    path('playlist/', views.playlist, name='playlist'),
    path('user/', views.user, name='user'),
    path('quangcao/', views.quangcao, name='quangcao'),
    path('theloai/', views.theloai, name='theloai'),
    path('chude/', views.chude, name='chude'),
]

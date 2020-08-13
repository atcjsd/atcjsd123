"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import project.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
# 메인
    path('main/', views.main),
    path('community/', views.community),
    
    #path('articlewrite/list/', views.list),
    path('articlewrite/list_buy/', views.list_buy),
    path('articlewrite/list_sale/', views.list_sale),
    path('articlewrite/list_free/', views.list_free),

    path('articlewrite/write_buy/', views.write_buy),
    path('articlewrite/write_free/', views.write_free),
    path('articlewrite/write_sale/', views.write_sale),

    path('articlewrite/detail_buy/<int:id>/', views.detail_buy),
    path('articlewrite/detail_free/<int:id>/', views.detail_free),
    path('articlewrite/detail_sale/<int:id>/', views.detail_sale),

    path('articlewrite/update_buy/<int:id>/', views.update_buy),
    
    # 회원가입    
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('signup/check_id/', views.check_id),

    #지도
    path('map/', views.map),    

]

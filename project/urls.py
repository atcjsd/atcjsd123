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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
# 메인
    path('sell/', views.sell),
    path('main/', views.main),
    path('community/', views.community),
    path('contact/', views.contact),
    
    #게시판
    #path('articlewrite/list/', views.list),
    path('articlewrite/list_buy/', views.list_buy),
    path('articlewrite/list_sale/', views.list_sale),
    path('articlewrite/list_free/', views.list_free),
    path('articlewrite/list_notic/', views.list_notic),

    #글작성
    path('articlewrite/write_buy/', views.write_buy),
    path('articlewrite/write_free/', views.write_free),
    path('articlewrite/write_sale/', views.write_sale),
    path('articlewrite/write_notic/', views.write_notic),

    #작성글
    path('articlewrite/detail_buy/<int:id>/', views.detail_buy),
    path('articlewrite/detail_free/<int:id>/', views.detail_free),
    path('articlewrite/detail_sale/<int:id>/', views.detail_sale),
    path('articlewrite/detail_notic/<int:id>/', views.detail_notic),

    #작성글 수정
    path('articlewrite/update_buy/<int:id>/', views.update_buy),
    path('articlewrite/update_free/<int:id>/', views.update_free),
    path('articlewrite/update_sale/<int:id>/', views.update_sale),
    path('articlewrite/update_notic/<int:id>/', views.update_notic),

    #작성글 삭제
    path('articlewrite/delete_buy/<int:id>/', views.delete_buy),
    path('articlewrite/delete_free/<int:id>/', views.delete_free),
    path('articlewrite/delete_sale/<int:id>/', views.delete_sale),
    path('articlewrite/delete_notic/<int:id>/', views.delete_notic),
    
    
    # 회원가입    
    path('signup/', views.signup),
<<<<<<< HEAD
=======
    path('signup_success/', views.signup_success),
>>>>>>> a9eb81440454177abc43e769764758fa9fba9283
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('signup/check_id/', views.check_id),

    #지도
    path('map/', views.map),    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

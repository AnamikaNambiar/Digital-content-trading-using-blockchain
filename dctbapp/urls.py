"""dctb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from dctbapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginn),
    path('login_post',views.login_post),
    path('complaintt',views.complaintt),
    path('viewfeedback',views.viewfeedback),
    path('viewuser', views.viewuser),
    path('reply/<id>', views.reply),
    path('reply_post/<id>',views.reply_post),
    path('changepswd', views.changepswd),
    path('changepswd_post',views.changepswd_post),
    path('homepage', views.homepage),

    # ==================================
    path('user_register',views.user_register),
    path('view_request',views.view_request),
    path('send_comp',views.send_comp),
    path('sendfeedback',views.sendfeedback),
    path('sendreq',views.sendreq),
    path('uploadimage',views.uploadimage),
    path('view_reply',views.view_reply),
    path('view_req_status',views.view_req_status),
    path('viewimage',views.viewimage),
    path('viewprofile',views.viewprofile),
    path('user_homepage',views.userhomepage),
    path('send_comp_post',views.send_comp_post),
    path('sendfeedback_post',views.sendfeedback_post),
    path('uploadimage_post',views.uploadimage_post),
    path('user_register_post',views.user_register_post),
    path('sendimgreq/<id>',views.sendimgreq),
    path('approvereq/<id>',views.approvereq),
    path('rejectreq/<id>',views.rejectreq),
    path('updateimage/<id>',views.updateimage),
    path('updateimage_post/<id>',views.updateimage_post),
    path('deleteimg/<id>',views.deleteimg),
    path('download_file_from_ipfs/<ipfs_hash>',views.download_file_from_ipfs),
    path('download_file_from_ipfs_video/<ipfs_hash>',views.download_file_from_ipfs_video),
    path('logout',views.logout),
    path('payment/<amount>/<id>',views.payment),
    path('paymentupdate',views.paymentupdate),
    path('viewothersimage',views.viewothersimage),

]

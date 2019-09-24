"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import app1view,dashview,d1view,d2view,du1view,du2view,du3view,du4view,frameview,lineview,line1view,newframeview,profileview,Tview,T0view,T1view,T2view,tableview,table1view,table2view,TD1view,TD2view,topview,top1view,top2view,userview,userprofileview,verticalview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('app1/',app1view),
    url('dash/',dashview),
    url('d1/',d1view),
    url('d2/',d2view),
    url('du1/',du1view),
    url('du2/',du2view),
    url('du3/',du3view),
    url('du4/',du4view),
    url('frame/',frameview),
    url('line/',lineview),
    url('line1/',line1view),
    url('newframe/',newframeview),
    url('profile/',profileview),
    url('T/',Tview),
    url('T0/',T0view),
    url('T1/',T1view),
    url('T2/',T2view),
    url('table/',tableview),
    url('table1/',table1view),
    url('table2/',table2view),
    url('TD1/',TD1view),
    url('TD2/',TD2view),
    url('top/',topview),
    url('top1/',top1view),
    url('top2/',top2view),
    url('user/',userview),
    url('userprofile/',userprofileview),
    url('vertical/',verticalview),

]

from django.conf.urls import url
from . import views
urlpatterns=[

        url(r'^$', views.app1view, name="views"),
        url(r'^dashboard/$', views.dashboardview, name="dashboard"),
            url(r'^newframe/$', views.newframeview, name="newframe"),
                url(r'^T/$', views.Tview, name="frame"),
                    url(r'^userprofile/$', views.userprofileview, name="userprofile"),

]

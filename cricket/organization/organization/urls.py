"""
URL configuration for commissioner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from os import name

from django.contrib import admin
from django.urls import path

from user import views

from organization import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showindex',views.showindex,name="showindex"),
    path('', views.showindex, name='showindex'),   # default page = index
    path('login', views.login, name='login'),
    path('insertnewuser', views.insertnewuser, name='insertnewuser'),
    path("forgotpassword",views.forgotpassword,name="forgotpassword"),
    path('showuser',views.showuser,name="showuser"),
    path('showadmin',views.showadmin,name="showadmin"),
    path('sendmail',views.sendmail,name='sendmail'),
    path('changepassword',views.changepassword,name='changepassword'),

    path('addorganizer',views.addorganizer,name="addorganizer"),
    path('addmatch_details',views.addmatch_details,name="addmatch_details"),
    path('addplayer_details',views.addplayer_details,name="addplayer_details"),
    path('addawards',views.addawards,name="addawards"),
    path('adduser_details',views.adduser_details,name="adduser_details"),
    path('addtplayer_statics',views.addtplayer_statics,name="addtplayer_statics"),
    path('addmatch_statics',views.addmatch_statics,name="addmatch_statics"),


    #View starts here
    path('vieworganizer',views.vieworganizer,name="vieworganizer"),
    path('viewmatch_details',views.viewmatch_details,name="viewmatch_details"),
    path('viewplayer_details',views.viewplayer_details,name="viewplayer_details"),
    path('viewawards',views.viewawards,name="viewawards"),

    path('viewuser_details',views.viewuser_details,name="viewuser_details"),
    path('viewplayer_statics',views.viewplayer_statics,name="viewplayer_statics"),
    path('viewmatch_statics',views.viewmatch_statics,name="viewmatch_statics"),

    # Delete start hear
    path('delawards/<int:pk>',views.delawards,name="delawards"),
    path('delorganizer/<int:pk>',views.delorganizer,name="delorganizer"),
    path('delmatch_details/<int:pk>',views.delmatch_details,name="delmatch_details"),
    path('delplayer_details/<int:pk>',views.delplayer_details,name="delplayer_details"),
    path('deluser_details/<int:pk>',views.deluser_details,name="deluser_details"),
    path('delplayer_statics/<int:pk>',views.delplayer_statics,name="delplayer_statics"),
    path('delmatch_statics/<int:pk>',views.delmatch_statics,name="delmatch_statics"),

    path('vieworg',views.vieworg,name="vieworg"),
    path('viewmatchdetail',views.viewmatchdetail,name="viewmatchdetail"),

    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
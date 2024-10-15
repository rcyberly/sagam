"""
URL configuration for sagam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from sagam import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sagamhome,name='sagamhome'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('sagamgems/',views.sagamgems,name='sagamgems'),
    path('sagamdharamshala/',views.sagamdharamshala,name='sagamdharamshala'),
    path('Ramkund/',views.Ramkund,name='Ramkund'),
    path('Places/',views.Places,name='Places'),
    path('news/',views.news,name='news'),
    path('Nagbalshivmandir/',views.Nagbalshivmandir,name='Nagbalshivmandir'),
    path('members/',views.members,name='members'),
    path('memberdetails/',views.memberdetails,name='memberdetails'),
    path('MataRadhaDevi/',views.MataRadhaDevi,name ='MataRadhaDevi'),
    path('Mataraageem/',views.Mataraageem,name='Mataraageem'),
    path('Home/',views.Home,name='Home'),
    path('Ganeshbal/',views.Ganeshbal,name='Ganeshbal'),
    path('gallary/',views.gallary,name='gallary'),
    path('Chandimata/',views.Chandimata,name='Chandimata'),
    
    
    ]
if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

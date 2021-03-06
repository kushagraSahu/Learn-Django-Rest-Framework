"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from quickstart import views

#Because we're using Viewsets instead of views, we can automatically generate the URL conf of our API, by simply registering the viewsets with a router class.
#If we need more control over the API urls we can simply drop down to using regular class based views, and writing the URL Conf explicitly.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)#Automatic generation of URL conf of our User API by registering the UserViewSet with the router class.
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),    
    url(r'^', include('snippets.urls')),
]
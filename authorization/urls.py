"""management URL Configuration

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
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/create/$', AdminCreateView.as_view()),
    url(r'^admin/invite/$', InviteUserView.as_view()),
    url(r'^admin/all/$', GetMyUsersView.as_view()),
    url(r'^login/', obtain_jwt_token),

    url(r'^register/(?P<username>[\w-]+)', CompleteUserRegistrationView.as_view()),
    url(r'^add/role/', RoleCreateView.as_view()),
]

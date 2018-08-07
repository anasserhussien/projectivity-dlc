from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [

    url(r'^$', ProjectListCreateAPIView.as_view() ),
    url(r'^(?P<pk>[0-9]+)/', ProjectRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^my/', MyProjectAPIView.as_view())

]

from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import *



class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUser,)
    def get_queryset(self):
        return Project.objects.filter(admin = self.request.user)


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUser,)

class MyProjectAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return user.admin.all()
        return user.assignee.all()

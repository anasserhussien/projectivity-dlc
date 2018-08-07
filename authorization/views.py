from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import(
    CreateAPIView, ListCreateAPIView,
    UpdateAPIView, ListAPIView)

from .serializers import *

# Create your views here.

class AdminCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminCreateSerializer

class InviteUserView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = InviteUserSerializer
    permission_classes = (IsAdminUser,)

class CompleteUserRegistrationView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CompleteUserRegistrationSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

class GetMyUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetMyUsersSerializer
    permission_classes = (IsAdminUser,)
    def get_queryset(self):
        user = self.request.user
        profiles = UserProfile.objects.filter(admin =user)
        list = []
        for pro in profiles:
            if pro.admin_id != pro.user_id:
                list.append(User.objects.get(pk = pro.user_id))
        return list

class RoleListCreateView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

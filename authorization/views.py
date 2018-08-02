from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import(
    CreateAPIView, ListCreateAPIView,
    UpdateAPIView)

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

class RoleCreateView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

import urllib.parse

class AdminCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_superuser')

    def create(self, validated_data):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = make_password(self.validated_data['password'])
        print (password,self.validated_data['is_superuser'] )
        is_superuser = self.validated_data['is_superuser']
        instance = User.objects.create(username = username, email = email, password = password,
            is_superuser = is_superuser, is_staff = True)
        instance.save()
        return instance


class InviteUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    full_url = ''
    class Meta:
        model = UserProfile
        fields = ('role','email')
    def create(self, validated_data):
        #print(self.context['request'].user)
        auto_generated_username = get_random_string(length = 30)
        while(User.objects.filter(username = auto_generated_username).first()):
            auto_generated_username = get_random_string(length = 30)
        username = auto_generated_username
        email = self.validated_data['email']
        role = get_object_or_404(Role, role = self.validated_data['role'])
        password = make_password(get_random_string(length = 100))

        instance = User(
            username = username,
            email = email,
            password = password,
            is_superuser = True if role.role == 'admin' else False,
            is_staff = True if role.role == 'admin' else False)
        instance.save()
        #send_mail('subject', 'body of the message', 'anasserhussien@fcih1.com', ['nasser@deemalab.com',])

        profile_instance = UserProfile(user = instance,
            role = role,
            admin_id = self.context['request'].user.id)
        profile_instance.save()
        base_url = self.context['request'].build_absolute_uri('/').strip("/")
        self.full_url += base_url + '/user/register/'+ username + '?query='
        query_params = urllib.parse.urlencode({"email":instance.email,
                                                "role": Role.objects.get(role = profile_instance.role)
                                                })
        self.full_url += query_params

        return profile_instance

    def to_representation(self, obj):
        return {
            'url': self.full_url,
        }



class CompleteUserRegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length = 128)
    last_name = serializers.CharField(max_length = 128)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def update(self, instance, validated_data):
        #instance.email = validated_data.get('email')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance


class GetMyUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name')



class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

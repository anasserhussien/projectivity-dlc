from rest_framework import serializers
from django.contrib.auth.models import User
from authorization.models import Role, UserProfile
from .models import *

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('admin',)

    def create(self, validated_data):
        #assignees = validated_data.pop('assignee')
        instance = Project.objects.create(
                    title = validated_data.get('title'),
                    desc = validated_data.get('desc'),
                    admin = self.context['request'].user)
        print(instance)
        instance.assignee = validated_data.get('assignee')
        instance.save()
        return instance

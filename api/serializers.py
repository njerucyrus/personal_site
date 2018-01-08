from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Skill, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all_', )


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'skill_name', )


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'project_title',
            'description',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'img_5',
            'date_started',
            'date_completed',
            'posted_on',

        )

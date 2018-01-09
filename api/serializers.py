from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Skill, Project, UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    profile_image = serializers.ImageField(max_length=False, use_url=True, allow_null=True, required=False)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone_number', 'secondary_email', 'profile_image')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'skill_name',)


class ProjectSerializer(serializers.ModelSerializer):
    img_1 = serializers.ImageField(max_length=None, use_url=True, required=False)
    img_2 = serializers.ImageField(max_length=None, use_url=True, required=False)
    img_3 = serializers.ImageField(max_length=None, use_url=True, required=False)
    img_4 = serializers.ImageField(max_length=None, use_url=True, required=False)
    img_5 = serializers.ImageField(max_length=None, use_url=True, required=False)

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

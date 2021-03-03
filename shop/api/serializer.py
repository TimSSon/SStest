from rest_framework import serializers
from accounts.models import Profile
from webapp.models import Item, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def validate(self, attrs):
        if get_user_model().objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email', ('Email is already in use')})
        return super().validate(attrs)



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('birth_date', 'avatar')


class UpdateUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data is not None:
            instance.profile.birth_date = profile_data['birth_date']
            instance.profile.avatar = profile_data['avatar']
            instance.profile.save()
        return super().update(instance, validated_data)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

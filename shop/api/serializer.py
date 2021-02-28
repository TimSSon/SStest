from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user', )
        # fields = ['name', 'avatar', 'phone', 'whatsapp', 'telegram']


class AdvertDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Advert
        fields = '__all__'


class AdvertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ('id', 'user', 'title', 'brand',
                  'model', 'body', 'price', 'photo')

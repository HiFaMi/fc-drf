from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

User = get_user_model()


class UserLoginSerializer(AuthTokenSerializer):

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            return serializers.ValidationError("존재하지 않는 아이디 입니다.")
        return value
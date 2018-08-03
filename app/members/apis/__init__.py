from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserLoginSerializer


class AuthToken(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user': UserLoginSerializer(user).data
            }
            return Response(data)
        raise AuthenticationFailed('인증정보가 올바르지 않습니다.')


class AuthenticationTest(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserLoginSerializer(request.user).data)
        raise NotAuthenticated('로그인 되어있지 않습니다.')

# Create your views here.
from rest_framework import generics, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from User.models import UsersModel
from User.permissions import IsAdminJWTPerimission
from User.serializers import UserSerializer, UserRegistrationSerializer


class UsersAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [AllowAny()]


class UsersListAPIView(generics.ListAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminJWTPerimission,)


class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserRegistrationSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class LogoutView(APIView):
    """Представления для выхода из системы"""

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]  # Получение токена
            token = RefreshToken(refresh_token)  # Создание токена
            token.blacklist()  # Помещение его в черный список
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

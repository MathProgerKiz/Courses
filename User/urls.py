from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from User.views import UsersAPIView, UsersListAPIView, UserViewSet, CustomTokenObtainPairView, LogoutView

urlpatterns = [
    path('all/', UsersListAPIView.as_view()),
    path('<int:pk>/', UsersAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/',UserViewSet.as_view({'post':'create'})),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='auth_logout')





]

from django.urls import path
from apps.user import views as user_views
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    #User Signup API
    path('signup/', user_views.UserSignUpAPIView.as_view(),name='user-signup'),
    path('login/',TokenObtainPairView.as_view(),name="user-email-login")
]
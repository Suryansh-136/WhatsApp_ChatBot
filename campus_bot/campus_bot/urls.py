from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Gakusei.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('token-login/',TokenObtainPairView.as_view()),
    path('refresh-token/',TokenRefreshView.as_view()),
  ] 
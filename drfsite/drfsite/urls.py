
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from women.views import *


# Видео 9
# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)
# router.register(r'category', CategoryViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDetail.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

# Видео 9

# Видео 9
#     path('api/v1/', include(router.urls)), # 127.0.0.1:8000/api/v1/women/

# Видео 8
#     path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})), # actions
#     path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})), # actions
# Видео 5
    # path('api/v1/womenlist/', WomenAPIView.as_view()),


# Видео 7
#     path('api/v1/womenlist/', WomenAPIList.as_view()),
#     path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
#     path('api/v1/womendetail/<int:pk>/', WomenAPIDetail.as_view()),
]

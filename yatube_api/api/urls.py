from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })
    ),
    path(
        'v1/follow/',
        FollowViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='jwt-create'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='jwt-refresh'
    ),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='jwt-verify'
    ),
]

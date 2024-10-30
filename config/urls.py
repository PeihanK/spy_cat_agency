from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from agency.views import CatViewSet, MissionViewSet, TargetViewSet


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'admin': request.build_absolute_uri('/admin/'),
        'cats': request.build_absolute_uri('/cats/'),
        'missions': request.build_absolute_uri('/missions/'),
        'targets': request.build_absolute_uri('/targets/'),
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('cats/', CatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cats/<int:pk>/', CatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('missions/', MissionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('missions/<int:pk>/', MissionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('targets/', TargetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('targets/<int:pk>/', TargetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

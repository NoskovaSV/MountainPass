from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from mount import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset, basename='users')
router.register(r'coords', views.CoordsViewset, basename='coords')
router.register(r'levels', views.LevelViewset, basename='levels')
router.register(r'images', views.ImageViewset, basename='images')
router.register(r'perevals', views.PerevalViewset, basename='perevals')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


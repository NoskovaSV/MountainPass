from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from mount import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'coords', views.CoordsViewset)
router.register(r'levels', views.LevelViewset)
router.register(r'images', views.ImageViewset)
router.register(r'perevals', views.PerevalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


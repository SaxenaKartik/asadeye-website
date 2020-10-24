from django.urls import path,include
from asadeye_api import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('product', views.ProductViewSet)
router.register('image', views.ImageViewSet)


urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
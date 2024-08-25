from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewset import cnpjViewSet


router = DefaultRouter()
router.register(prefix="f1", viewset=cnpjViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewset import cnpjViewSet


router = DefaultRouter()
router.register(prefix="cnpj", viewset=cnpjViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
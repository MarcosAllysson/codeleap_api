from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api.viewsets import PostViewSet

router = DefaultRouter()
router.register(r"", PostViewSet, basename="post")

urlpatterns = router.urls

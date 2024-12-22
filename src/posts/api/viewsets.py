from rest_framework import viewsets
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer, PostUpdateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "partial_update":
            return PostUpdateSerializer
        return PostSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.username != request.data.get("username", instance.username):
            return Response({"detail": "Username cannot be modified"}, status=400)
        return super().partial_update(request, *args, **kwargs)

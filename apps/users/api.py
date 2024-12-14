from typing import Any

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer: Any) -> Response:
        serializer.save(username=self.request.user.username)
        return Response({"success": "Post created successfully."}, status=status.HTTP_201_OK)

    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        post = self.get_object()
        if post.username != request.user.username:
            return Response({'error': 'You can only edit your own posts.'}, status=status.HTTP_403_FORBIDDEN)
        
        partial_data = request.data.copy()
        restricted_fields = ['id', 'username', 'created_at']
        for field in restricted_fields:
            partial_data.pop(field, None)
        
        serializer = self.get_serializer(post, data=partial_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        post = self.get_object()
        if post.username != request.user.username:
            return Response({'error': 'You can only delete your own posts.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

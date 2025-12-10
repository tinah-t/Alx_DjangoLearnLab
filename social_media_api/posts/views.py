from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
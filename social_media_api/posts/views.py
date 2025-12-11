from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from accounts.models import CustomerUser

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class FeedView(generics.ListAPIView):
    #  permissions.IsAuthenticated
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        all_users = CustomerUser.objects.all() 
        following_users = self.request.user.following.all() 
        return Post.objects.filter(author__in=following_users).order_by('-created_at')        

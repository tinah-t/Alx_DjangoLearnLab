from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment, Like
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.models import CustomerUser
from rest_framework.views import APIView
from notifications.models import Notification

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

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)
        if Like.objects.filter(user=user,post=post).exists():
            return Response({"detail":"You have already liked this post."},status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(user=user,post=post)
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)

        like = Like.objects.filter(user=user, post=post).first()

        if not like:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

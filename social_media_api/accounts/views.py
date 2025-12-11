from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from .models import CustomerUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .tokens import create_jwt_pair_for_user
from django.shortcuts import get_object_or_404
from posts.serializers import PostSerializer
from posts.models import Post


User = CustomerUser



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # username = serializer.validated_data["username"]
        # password = serializer.validated_data["password"]
        # user = authenticate(username=username, password=password)
        user = serializer.validated_data["user"]
        # tokens = create_jwt_pair_for_user(user)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
#  permissions.IsAuthenticated
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    #  CustomUser.objects.all()
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomerUser, id=user_id)
        if request.user.id == target_user.id:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST)
        target_user.followers.add(request.user)
        request.user.following.add(target_user)
        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK)
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    all_users = CustomerUser.objects.all()
    #  CustomUser.objects.all()
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomerUser, id=user_id)
        if request.user.id == target_user.id:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        target_user.followers.remove(request.user)
        request.user.following.remove(target_user)
        return Response(
            {"detail": f"You unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )

class FeedView(generics.ListAPIView):
    #  permissions.IsAuthenticated
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        all_users = CustomerUser.objects.all() 
        following_users = self.request.user.following.all() 
        return Post.objects.filter(author__in=following_users).order_by('-created_at')        

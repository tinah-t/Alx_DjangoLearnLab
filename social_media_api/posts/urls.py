from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
# What this does

# GET /posts/ → List all posts
# POST /posts/ → Create a new post
# GET /posts/<id>/ → Retrieve a post
# PUT /posts/<id>/ → Update a post
# PATCH /posts/<id>/ → Partial update
# DELETE /posts/<id>/ → Delete a post
# Same for comments:
# GET /comments/
# POST /comments/
# GET /comments/<id>/
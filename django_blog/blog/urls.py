from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, profile_view, edit_profile, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, CommentCreateView,CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', next_page='/list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html', next_page='/create'), name='logout'),
    path('register/', signup, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('post/new/', BlogCreateView.as_view(),name='blog_create'),
    path('posts/', BlogListView.as_view(),name='blog_list'),
    path('posts/<int:pk>/', BlogDetailView.as_view(),name='blog_detail'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(),name='blog_update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(),name='blog_delete'),
    path('post/<int:pk>/comments/new/',CommentCreateView.as_view(),name="comment_create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),


]

# {% if user.is_authenticated %}
#           <li>
#             <a href="{% url 'logout' %}">Log out</a>
#           </li>
#           {% else %}
#           <li><a href="{% url 'login' %}">Login</a></li>
#           <li><a href="{% url 'register' %}">Register</a></li>
#           {% endif  %}
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, profile_view, edit_profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html', next_page='/login'), name='logout'),
    path('register/', signup, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
]

# {% if user.is_authenticated %}
#           <li>
#             <a href="{% url 'logout' %}">Log out</a>
#           </li>
#           {% else %}
#           <li><a href="{% url 'login' %}">Login</a></li>
#           <li><a href="{% url 'register' %}">Register</a></li>
#           {% endif  %}
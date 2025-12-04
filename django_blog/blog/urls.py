from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]

# {% if user.is_authenticated %}
#           <li>
#             <a href="{% url 'logout' %}">Log out</a>
#           </li>
#           {% else %}
#           <li><a href="{% url 'login' %}">Login</a></li>
#           <li><a href="{% url 'register' %}">Register</a></li>
#           {% endif  %}
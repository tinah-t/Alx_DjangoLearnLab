from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('hello/', views.list_books,name='hello'),
    path('about/<int:pk>/', views.LibraryDetailView.as_view(),name='about'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')), 
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'))
]
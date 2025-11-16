from django.urls import path
from .views import list_books, LibraryDetailView,SignUpView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('hello/', list_books,name='hello'),
    path('about/<int:pk>/', LibraryDetailView.as_view(),name='about'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')), 
    path('register/', SignUpView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'))
]
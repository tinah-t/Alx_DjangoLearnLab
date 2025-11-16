from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('books/', views.list_books,name='books'),
    path('about/<int:pk>/', views.LibraryDetailView.as_view(),name='about'),
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')), 
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'))
]
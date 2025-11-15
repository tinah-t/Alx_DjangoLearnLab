from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('hello/', list_books,name='hello'),
    path('about/<int:pk>/', LibraryDetailView.as_view(),name='about')

]
from django.urls import path
from .views import list_books, LibraryDetailView
url_patterns=[
    path('hello/', list_books,name='hello'),
    path('about/', LibraryDetailView.as_view(),name='about')

]
from django.urls import path
from .views import BookCreateView, BookDetailView, BookDeleteView, BookListView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view() , name='book_list'),
    path('books/create/', BookCreateView.as_view() , name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view() , name='book_detail'),
     path('books/<int:pk>/update/', BookUpdateView.as_view() , name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view() , name='book_delete'),
    #  path('books/update/', BookUpdateView.as_view() , name='book_update'),
    # path('books/delete/', BookDeleteView.as_view() , name='book_delete'),
]
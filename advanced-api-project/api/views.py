from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
       title = serializer.validated_data.get('title')
       if Book.objects.filter(title=title).exists():
            raise serializer.errors("A book with this title already exists.")
       serializer.save()
# @permission_classes([IsAuthenticated])
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_update(self, serializer):
        book = self.get_object()

        # Custom permission rule: only admins can update
        # if not self.request.user.is_staff:
            #\ raise PermissionError("Only admins can modify books.")

        # Example: Ensure unique title on update
        new_title = serializer.validated_data.get("title", book.title)
        if Book.objects.exclude(pk=book.pk).filter(title=new_title).exists():
            raise PermissionError("Another book with this title already exists.")

        serializer.save()
# @permission_classes([IsAuthenticated])
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

# @permission_classes([IsAuthenticatedOrReadOnly])
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

# @permission_classes([IsAuthenticatedOrReadOnly])
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

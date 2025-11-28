from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("The publication date must be corrected!")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.CharField(source='book.name', read_only=True)
    class Meta:
        model = Author
        fields = ['name','books']
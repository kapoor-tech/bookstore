from rest_framework import serializers # type: ignore
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'price', 'amazon_url']

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # filtrowanie po wielu polach
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['author', 'year']

    # wyszukiwanie tekstowe
    search_fields = ['title', 'author']

    # sortowanie
    ordering_fields = ['title', 'year']
    ordering = ['title']

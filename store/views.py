from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import filters

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    # filterset_fields = ['category','writer']
    # ordering_fields = ['name','price','stock','totalreview','totalrating']
    # search_filelds = ['name','descriptions']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class GenreBooksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre_name = self.kwargs['genre_name']
        return Book.objects.filter(genre__name__iexact=genre_name)

class WriterBooksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        writer_name = self.kwargs['writer_name']
        return Book.objects.filter(writer__name__iexact=writer_name)

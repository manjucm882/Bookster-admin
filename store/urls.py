from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('genre',GenreViewSet)
router.register('writer',WriterViewSet)
router.register('books',BookViewSet)
router.register('review',ReviewViewSet)
router.register('slider',SliderViewSet)
router.register(r'genre/(?P<genre_name>[\w-]+)/books',GenreBooksViewSet,basename='genre-books')
router.register(r'writer/(?P<writer_name>[\w-]+)/books', WriterBooksViewSet, basename='writer-books')


urlpatterns = [
    path('',include(router.urls)),
]
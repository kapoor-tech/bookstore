from django.urls import path # type: ignore
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]

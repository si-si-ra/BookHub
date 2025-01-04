from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailsView.as_view(), name='book-details'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/search/', search_books, name='book-search'),

]
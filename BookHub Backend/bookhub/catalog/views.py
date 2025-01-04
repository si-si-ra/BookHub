# catalog/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny

# Add Book to Catalog
class BookCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class=[AllowAny]
    
class BookDetailsView (generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

# Update Book Information
class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Delete Book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 

# Search for Books
@api_view(['GET'])
def search_books(request):
    query = Q()
    if 'author' in request.GET:
        query &= Q(author__icontains=request.GET['author'])
    if 'isbn' in request.GET:
        query &= Q(isbn=request.GET['isbn'])
    if 'published_year' in request.GET:
        query &= Q(published_year=request.GET['published_year'])
    if 'subjects' in request.GET:
        subjects = request.GET['subjects'].split(',')
        query &= Q(subjects__contains=subjects)
    if 'places' in request.GET:
        places = request.GET['places'].split(',')
        query &= Q(places__contains=places)
    
    books = Book.objects.filter(query)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



























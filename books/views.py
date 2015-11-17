
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book, Publisher

# Create your views here.
class BookListView(ListView):
    model = Book

    def head(self,*args,**kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse()
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

class PublisherList(ListView):
    model = Publisher



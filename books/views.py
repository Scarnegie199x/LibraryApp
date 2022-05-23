from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

class AddBook(CreateView):
    model = Book
    template_name = "new_book.html"
    fields = ['title', 'subtitle','author','isbn']

# Create your views here.



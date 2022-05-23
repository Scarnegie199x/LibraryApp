from django.urls import path
from .views import BookListView, AddBook

urlpatterns = [
    path("new/", AddBook.as_view(), name = "add_book"),
    path("", BookListView.as_view(), name = "home"),
]
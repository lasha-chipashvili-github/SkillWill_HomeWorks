from django.shortcuts import render
# from django.http import HttpResponse
from .forms import BookForm
from .models import Book


# Create your views here.
def book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'books.html', context=context)


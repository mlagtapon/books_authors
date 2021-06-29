from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):

    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request, 'index.html', context)

def authors(request):

    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def get_book(request, book_id):

    onebook = Book.objects.get(id=book_id)
    all_authors = Book.objects.get(id=book_id).authors.all()

    context = {
        "all_the_authors": Author.objects.all(),
        "onebook": onebook,
        "all_authors": all_authors
    }
    return render(request, 'books.html', context)

def get_author(request, author_id):

    oneauthor = Author.objects.get(id=author_id)
    all_books = Author.objects.get(id=author_id).books.all()

    context = {
        "all_the_books": Book.objects.all(),
        "oneauthor": oneauthor,
        "all_books": all_books
    }
    return render(request, 'viewauthors.html', context)

def add_book(request):

    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])

    return redirect('/')

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])

    return redirect('/authors')

def add_author_to_book(request):

    book_id = request.POST['book_id']
    author_id = request.POST['author']
    
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=author_id)
    this_author.books.add(this_book)

    return redirect('/books/'+ book_id)

def add_book_to_author(request):

    book_id = request.POST['book']
    author_id = request.POST['author_id']
    
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=author_id)
    this_book.authors.add(this_author)

    return redirect('/authors/'+ author_id)
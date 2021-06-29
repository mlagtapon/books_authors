from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:book_id>/', views.get_book),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('authors/<int:author_id>/', views.get_author),
    path('add_author_to_book', views.add_author_to_book),
    path('add_book_to_author', views.add_book_to_author),
]
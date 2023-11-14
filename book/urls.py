from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/<str:pk>/', views.book, name='single-book'),
]

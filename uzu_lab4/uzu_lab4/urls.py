# plik biblioteka/urls.py

from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('admin/', admin.site.urls),
    path('biblioteka/', include('biblioteka.urls')),
    path("books_cbv/", views.BookListView.as_view(), name="book-list"),
    path("books_cbv/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
]



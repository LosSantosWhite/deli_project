from django.urls import path
from books.views import BookDetailView, BookCreateView, ValidateBookName
app_name = 'books'

urlpatterns = [
    path('<int:pk>/', BookDetailView.as_view(), name='detail_view'),
    path('create/', BookCreateView.as_view(), name='create_view'),
    path('validate-name/', ValidateBookName.as_view(), name='validate_book_name_view')

]
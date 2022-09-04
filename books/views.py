import json

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from books.models import Book


class BookDetailView(DetailView):
    context_object_name = 'book'
    template_name = 'detail.html'

    def get_object(self, queryset=None):
        return Book.objects.get(id=self.kwargs['pk'])


class BookListView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name = 'list.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login_view')
    model = Book
    template_name = 'create.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BookCreateView, self).form_valid(form)


class ValidateBookName(View):
    def get(self, request):
        book_name = request.GET.get("bookName")
        try:
            Book.objects.get(name__exact=book_name)
            return JsonResponse({"status": "failed",
                                 "book_error": "Такая книга уже есть!"})
        except Book.DoesNotExist:
            return JsonResponse({"status": "ok"}, status=200)

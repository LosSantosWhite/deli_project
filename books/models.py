from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Book(models.Model):
    name = models.CharField('Название книги', max_length=100, unique=True)
    author = models.ForeignKey(CustomUser, verbose_name='Автор книги', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def get_absolute_url(self):
        return reverse('books:detail_view', args=[self.id])

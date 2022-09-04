from django.test import TestCase
from django.urls import reverse
from books.models import Book, CustomUser

BOOKS_COUNT = 5
USER = {'username': 'test_user',
        'password': 'TestPassword1234',
        'first_name': 'Name',
        'last_name': 'Lastname',
        'surname': 'Surname'}


class TestBookView(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(
            **USER
        )
        for book in range(BOOKS_COUNT):
            Book.objects.create(
                name=str(book),
                author=user
            )

    def test_get_list_view(self):
        response = self.client.get(reverse('books:list_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(
            len(response.context['books']), BOOKS_COUNT
        )

    def test_get_detail_view(self):
        response = self.client.get(reverse('books:detail_view', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')

    def test_create_view_without_login(self):
        response = self.client.post(reverse('books:create_view'),
                                    data={'name': 'Название книги', 'author': USER['username']})
        self.assertEqual(len(Book.objects.all()), BOOKS_COUNT)
        self.assertEqual(response.status_code, 302)

    def test_create_view_with_login(self):
        print(self.client.login(username=USER['username'], password=USER['password']))
        response = self.client.post(reverse('books:create_view'),
                                    data={'name': 'Название книги', 'author': USER['username']})
        print(response)
        self.assertEqual(len(Book.objects.all()), BOOKS_COUNT+1)

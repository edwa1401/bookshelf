from django.test import Client, TestCase

from books.models import Book

client = Client()


def create_book(
        title,
        author_full_name,
        year_of_publishing,
        copies_printed,
        short_description
        ):
    return Book.objects.create(
        title=title,
        author_full_name=author_full_name,
        year_of_publishing=year_of_publishing,
        copies_printed=copies_printed,
        short_description=short_description
    )


class QuestionIndexViewTests(TestCase):
    def test__get_books__success(self):
        book_1 = create_book(
            title='any_book',
            author_full_name='nobody',
            year_of_publishing=2000,
            copies_printed=2,
            short_description='book about nothing'
            )
        response = self.client.get('/books/')
        self.assertQuerysetEqual(
            response.context['books'],
            [book_1]
        )
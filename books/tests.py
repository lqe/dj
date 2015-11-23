from django.test import TestCase

from books.models import BookTest1

class BookTest1TestCase(TestCase):
    def setUp(self):
        BookTest1.objects.create(name='book1', price=2.3)
        BookTest1.objects.create(name='book2', price=2.4)

    def test_booktest1_has_price(self):
        from decimal import Decimal
        book1 = BookTest1.objects.get(name='book1')
        book2 = BookTest1.objects.get(name='book2')
        self.assertEqual(book1.price, Decimal('2.30'))
        self.assertEqual(book2.price, Decimal('2.40'))




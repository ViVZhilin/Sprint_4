import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize(
        'books_list, genre',
        [
            ['Капитан Америка', 'Фантастика'],
            ['Достать ножи', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre(self, books_list, genre):
        collector = BooksCollector()

        books = {
            'Капитан Америка': 'Фантастика',
            'Достать ножи': 'Детективы'
        }

        for keys, values in books.items():
            collector.add_new_book(keys)
            collector.set_book_genre(keys, values)

        assert collector.get_books_with_specific_genre(genre) == [books_list]


    def test_get_books_genre_empty_dictionary(self):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_filled_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_genre() == {
            'Гордость и предубеждение и зомби' : 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }

    def test_get_books_for_children_add_two_child_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        collector.add_new_book('Улица Сезам')
        collector.set_book_genre('Улица Сезам', 'Мультфильмы')

        collector.add_new_book('Тотошка')
        collector.set_book_genre('Тотошка', 'Комедии')

        assert collector.get_books_for_children() == ['Улица Сезам', 'Тотошка']

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Как выспаться?')
        collector.add_new_book('Страх и ненависть в Лас-Вегасе')
        collector.add_new_book('Юмористическое пособие для пессимистов')


        collector.add_book_in_favorites('Как выспаться?')
        collector.add_book_in_favorites('Юмористическое пособие для пессимистов')

        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Как выспаться?')
        collector.add_new_book('Страх и ненависть в Лас-Вегасе')
        collector.add_new_book('Юмористическое пособие для пессимистов')

        collector.add_book_in_favorites('Как выспаться?')
        collector.add_book_in_favorites('Юмористическое пособие для пессимистов')

        collector.delete_book_from_favorites('Как выспаться?')

        assert len(collector.favorites) == 1


    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Как выспаться?')
        collector.add_new_book('Страх и ненависть в Лас-Вегасе')
        collector.add_new_book('Юмористическое пособие для пессимистов')

        collector.add_book_in_favorites('Как выспаться?')
        collector.add_book_in_favorites('Юмористическое пособие для пессимистов')

        assert collector.favorites == ['Как выспаться?', 'Юмористическое пособие для пессимистов']





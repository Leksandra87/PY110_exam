MODEL = "shop_final.book"

from random import choice
import re

BOOKS_FILE = 'books.txt'
BOOK_REGEX = r'100.+\s\—\s(?P<Title>.+?)\n'
"""
Декоратор 'check_title' проверяет длинну строки, выходящей из функции 'find_title'. Если количество символов больше
 заданного значения, вместо названия книги вписывается текст "Слишком длинное название"
"""


def check_title(fn):
    def wrapper():
        while True:
            title = next(fn())
            if len(title) <= 12:
                yield title
            else:
                yield "Слишком длинное название"

    return wrapper


'''
Функция find_title() находит названия книг в текстовом файле books.txt, собирает их в список и выдает в случайном порядке.
'''


@check_title
def find_title() -> str:
    book_pattern = re.compile(BOOK_REGEX)
    with open(BOOKS_FILE, "r", encoding="utf-8") as books:
        title = [book.groupdict() for book in book_pattern.finditer(books.read())]
    while True:
        yield choice(title)['Title']


TITLE = find_title()

if __name__ == '__main__':
    for _ in range(5):
        print(next(TITLE))

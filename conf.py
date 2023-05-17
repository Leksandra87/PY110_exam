MODEL = "shop_final.book"

from random import choice
import re

BOOKS_FILE = 'books.txt'
BOOK_REGEX = r'100.+\s\—\s(?P<Title>.+?)\n'

'''
Функция find_title() находит названия книг в текстовом файле books.txt, собирает их в список и выдает в случайном порядке.
'''


def find_title() -> str:
    book_pattern = re.compile(BOOK_REGEX)
    with open(BOOKS_FILE, "r", encoding="utf-8") as books:
        title = [book.groupdict() for book in book_pattern.finditer(books.read())]
    while True:
        yield choice(title)['Title']


TITLE = find_title()

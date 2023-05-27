from faker import Faker

f = Faker()

import random, conf, json


def dict_gen(n: int = 1) -> dict:
    """
    Функция генерирует случайные словари по одному
    :param n:
    :return:
    """
    while True:
        d = {"model": conf.MODEL,
             "pk": n,
             "fields": {
                 "title": next(conf.TITLE),
                 "year": f.year(),
                 "pages": random.randint(5, 1000),
                 "isbn13": f.isbn13(),
                 "rating": round(random.uniform(0, 5.01), 2),
                 "price": random.randint(300, 5000),
                 "author": [f.name() for _ in range(random.randint(1, 3))]
             }}
        yield d
        n += 1


def main(n: int = 100):
    """
    Функция создает список случайных словарей и записывает в json - файл.
    передаваемый параметр 'n' - количество словарей в списке
    :param n:
    :return:
    """
    dat = dict_gen()
    libra = [next(dat) for _ in range(n)]
    with open('new.json', 'w', encoding="utf-8") as n:
        json.dump(libra, n, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main(20)

# Строки в Питоне сравниваются на основании значений символов.
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
class RealString:
    def __init__(self, str_1):
        self.str_1 = str(str_1)

    def __eq__(self, other):  # ==
        if isinstance(other, RealString):
            return len(self.str_1) == len(other.str_1)

    def __lt__(self, other):  # <
        if isinstance(other, RealString):
            return len(self.str_1) < len(other.str_1)

    def __gt__(self, other):  # >
        if isinstance(other, RealString):
            return len(self.str_1) > len(other.str_1)


stroc_1 = RealString('hellooo')
stroc_2 = RealString('привет')
print(stroc_1 == stroc_2)
print(stroc_1 < stroc_2)
print(stroc_1 > stroc_2)
#print(ord('A'))

print()

# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку
# (например, по автору или по году издания), добавления книг в библиотеку, удаления книг из нее,
# сортировки книг по разным полям.
class HomeLibrary:
    library = {}
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.library.update({name: [author, year]})

    def adding_book(self, name, author, year):  # добавление книг
        self.library.update({name: [author, year]})
        return self.library

    def search_book(self, name, library):  # поиск книг
        if name not in library:
            print('Книга не найдена')
        else:
            print(name, library.get(name))

    def delete_book(self, name, library):  # удаления книг
        if name not in library:
            print('Книга не найдена')
        else:
            library.pop(name)
            print(library)

    def sorted_book(self, library):  # сортировка книг
        sorted_library = {}
        sorted_key = sorted(library, key=library.get)
        for val in sorted_key:
            sorted_library[val] = library[val]
        print(sorted_library)



lib = HomeLibrary('Emma', 'Ostin', '2003')
print(lib.library)
print(lib.adding_book('Jony', 'London', '1992'))
print(lib.library)
print(lib.search_book('Emma', lib.library))
print(lib.sorted_book(lib.library))
print(lib.delete_book('Emma', lib.library))













# С помощью классов создать новый тип данных изменяемая строка
# Можно добавить изменение через метод или через магические методы
# Подсказка: строка это массив (список) char
# res = 'str'.replace('s','r')
# print(res)
# res = [1, 2, 3]
# res[0] = 3
# print(res)
#
# my_str = 'hello, world'  # в результате выполнения задания id должны быть одинаковые
# print(id(my_str))
# result = my_str.replace('h', 'q')
# print(id(result))

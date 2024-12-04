import json
import random
import time

class Book:
    def __init__(self, 
                 title: str, 
                 author: str,
                 year: int):
        self.id = random.randint(100000, 999999)
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'

    def add_book(self):
        book_dict = {}
        with open('library.json', 'a', encoding='utf-8') as file:
            json.dump(book_dict, file)

    @staticmethod
    def delete_book():
        pass

    @staticmethod
    def search_book():
        pass

    @staticmethod
    def select_all_books():
        pass

    @staticmethod
    def change_status_book():
        pass

if __name__ == "__main__":
    menu_dict = {
            1: 'Добавить книгу',
            2: 'Удалить книгу',
            3: 'Поиск книги',
            4: 'Вывести все книги',
            5: 'Изменить статус книги',
            6: 'Выход из программы'
        }
    signal = True

    while signal:      
        print('Выберите пункт меню:')
        for number, value in menu_dict.items():
            print(f'{number}) {value}') 

        try:
            user_number = int(input('>'))
            
            if user_number == 6:
                signal = False
            
            if user_number not in menu_dict:
                print('WARNING: Такого пункта меню не существует!')
                time.sleep(2.0)
            
            if user_number == 1:
                title = input('Название книги:')
                author = input('ФИО автора:')
                year = input('Год:')
                book = Book(title = title,
                            author = author,
                            year = year,)
                book.add_book()
                print('INFO: Книга создана!')
                time.sleep(1.0)
        
        except:
            print('WARNING: Введите пожалуйста число!')
            time.sleep(2.0)

        